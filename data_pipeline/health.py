import datetime
import json

import xmltodict
import pandas as pd

from data_pipeline.utils import _parse_float, _parse_date, _parse_device_string, _parse_source_id, put_json, put_dataframe
from consts import *

class HealthKitData:
    '''
    XML HealthKit data. All data is sorted by date low-to-high
    '''

    def __init__(self, file):
        if type(file) == dict:
            self.data = file
        else:
            self.file = file
            self.config = {}
            self.data = None
            print('Reading export file...')
            with open(file) as file:
                xml = xmltodict.parse(file.read())
                self.data = xml["HealthData"]
        print('Processing Data...')
        self.config = self._get_config()
        self.activity_summaries = self._get_activity_summaries()
        self.workouts = self._get_workouts()
        self.records = self._get_records()

    def set_sources(self, sources):
        self.config['sources'] = sources

    def save(self, save_path):
        data = {
            'activity_summaries.json': self.activity_summaries,
            'config.json': self.config,
            'workouts.parquet': self.workouts,
            'records.parquet': self.records,

        }
        for key, obj in data.items():
            print(f"Saving: {key}")
            if '.json' in key:
                put_json(obj, path=f'{save_path}{key}')
            elif key == 'workouts.parquet':
                df = pd.DataFrame(obj)
                df['last_updated'] = datetime.datetime.now()
                put_dataframe(df, path=f'{save_path}{key}')
            elif key == 'records.parquet':
                df = pd.DataFrame(obj)
                df['last_updated'] = datetime.datetime.now()
                put_dataframe(df, path=f'{save_path}{key}')
            else:
                raise Exception(f'Invalid Key: {key} to save')




    def _get_records(self):
        """
        Parse Records from Payload and update config sources with record device sources
        Return a dict
        """
        sources = {}

        records = self.data['Record']#self.data.pop('Record', [])
        out = []
        for r in records:
            rec = Record(**r)
            sources.update(self._parse_source(r))
            out.append(rec.__dict__)

        self.set_sources(sources)
        return out

    def _parse_source(self, data):
        """
        Parse Sources from Payload
        Return a dict
        """
        source_name = data.get(SOURCE_NAME)

        source_type = "UNKNOWN"
        if 'WATCH' in source_name.upper():
            source_type = 'WATCH'
        elif 'RENPHO' in source_name.upper():
            source_type = 'SCALE'
        elif 'PHONE' in source_name.upper():
            source_type = 'PHONE'
        elif 'MYFITNESSPAL' in source_name.upper():
            source_type = 'APP'
        elif 'HEALTH' in source_name.upper():
            source_type = 'APP'  # manually entered value into health app
        elif 'STRONG' in source_name.upper():
            source_type = 'APP'
        elif 'SLEEP' in source_name.upper():
            source_type = 'APP'

        source_version = data.get(SOURCE_VERSION, None)
        source_id = _parse_source_id(source_name)
        device = data.get(DEVICE, None)
        source = {
            "source_name": source_name,
            "source_version": source_version,
            "source_type": source_type,
        }
        if device is not None:
            source = {
                **source,
                **_parse_device_string(device)
            }

        return {source_id: source}

    def _get_config(self):
        """
        Parse Config from Payload from Me, ExportDate and Unique Devices found in Records
        Return a dict
        """
        me = self.data['Me']#self.data.pop('Me', {})
        export_date = self.data['ExportDate']#self.data.pop('ExportDate', {})
        dob = _parse_date(me.get(HK_ME_DATE_OF_BIRTH))

        return {
            'date_of_birth': dob,
            'age': (datetime.datetime.now() - dob.to_pydatetime()).days // 365, # For comparison convert both to datetime.datetime to get datetime.timedelta
            'biological_sex': me.get(HK_ME_BIOLOGICAL_SEX),
            'blood_type': me.get(HK_ME_BLOOD_TYPE),
            'skin_type': me.get(HK_ME_SKIN_TYPE),
            'wheelchair_use': me.get(HK_ME_WHEELCHAIR_USE),
            'sources': {},
            'goals': {
                'active_energy_burned_goal': None,
                'move_time_goal': None,
                'exercise_time_goal': None,
                'stand_hours_goal': None,
                'sleep_goal': None,
            },
            'last_updated': pd.Timestamp(export_date['@value']),
        }

    def _get_activity_summaries(self):
        """
        Parse ActivitySummaries from Payload
        Return a dict of {date: {key: value}}
        """
        activity_summaries = self.data['ActivitySummary']  # self.data.pop('ActivitySummary', [])

        parsed = {}
        for activity_summary in activity_summaries:
            date = activity_summary.get(DATE_COMPONENTS)
            parsed[date] = {
                'active_energy_burned': _parse_float(activity_summary.get(ACTIVE_ENERGY_BURNED, None)),
                'active_energy_burned_goal': _parse_float(activity_summary.get(ACTIVE_ENERGY_BURNED_GOAL, None)),
                'active_energy_burned_unit': activity_summary.get(ACTIVE_ENERGY_BURNED_UNIT, "Cal"),
                'move_time': _parse_float(activity_summary.get(APPLE_MOVE_TIME, None)),
                'move_time_goal': _parse_float(activity_summary.get(APPLE_EXERCISE_TIME_GOAL, None)),
                'exercise_time': _parse_float(activity_summary.get(APPLE_EXERCISE_TIME, None)),
                'exercise_time_goal': _parse_float(activity_summary.get(APPLE_EXERCISE_TIME_GOAL, None)),
                'stand_hours': _parse_float(activity_summary.get(APPLE_STAND_HOURS, None)),
                'stand_hours_goal': _parse_float(activity_summary.get(APPLE_STAND_HOURS_GOAL, None)),
            }
        return parsed

    def _get_workouts(self):
        workouts = self.data['Workout']#self.data.pop('Workout', [])
        return [Workout(**w).__dict__ for w in workouts]


class Record:
    NAME_KEY = TYPE

    def __init__(self, **data):
        """
        Parse a Record from the Payload, handle metadata creation and source_id
        """
        self.name: str = data[self.NAME_KEY]
        self.source_id = _parse_source_id(data.get(SOURCE_NAME))
        self.created_at: pd.Timestamp = _parse_date(data.get(CREATION_DATE, None))
        self.start: pd.Timestamp = _parse_date(data.get(START_DATE))
        self.start_date_str: str = self.start.strftime("%Y-%m-%d")
        self.end: pd.Timestamp = _parse_date(data.get(END_DATE))
        self.unit: str = data.get(UNIT, None)
        self.value: float = _parse_float(data.get(VALUE, None))
        self.heartrate_variability = []

        metadata = data.get("MetadataEntry", None)
        if metadata is None:
            self.metadata = []
        elif isinstance(metadata, dict):
            self.metadata = [self._parse_metadata(metadata)]
        elif isinstance(metadata, list):
            self.metadata = list(map(lambda m: self._parse_metadata(m), metadata))

        heartrate_variability = data.get("HeartRateVariabilityMetadataList", None)
        if heartrate_variability is not None:
            heartrate_variability = heartrate_variability.get("InstantaneousBeatsPerMinute", None)
            self.heartrate_variability = list(map(lambda m: self._parse_heartrate_variability(m), heartrate_variability))

    def _parse_metadata(self, data):
        return {'key': data.get(KEY), 'value': data.get(VALUE)}

    def _parse_heartrate_variability(self, data):
        return {'bpm': data.get(BPM), 'time': _parse_date(data.get(TIME))}


class Workout(Record):
    NAME_KEY = WORKOUT_ACTIVITY_TYPE

    def __init__(self, **data):
        super().__init__(**data)
        self.duration: float = _parse_float(data.get(DURATION))
        self.duration_unit: str = data.get(DURATION_UNIT)

        self.distance: float = _parse_float(data.get(TOTAL_DISTANCE, None))
        self.distance_unit: str = data.get(TOTAL_DISTANCE_UNIT, 'mi')

        self.energy_burned: float = _parse_float(data.get(TOTAL_ENERGY_BURNED, None))
        self.energy_burned_unit: str = data.get(TOTAL_ENERGY_BURNED_UNIT, 'Cal')

        self.flights_climbed: float = _parse_float(data.get(TOTAL_FLIGHTS_CLIMBED))
        self.swimming_strokes: float = _parse_float(data.get(TOTAL_SWIMMING_STROKE_COUNT))
        self.events = []
        self.statistics = []
        self.route = None

        workout_events = data.get("WorkoutEvent", None)
        if workout_events is not None:
            if isinstance(workout_events, dict):
                self.events = [self._parse_workout_event(workout_events)]
            else:
                self.events = list(map(lambda m: self._parse_workout_event(m), workout_events))

        workout_statistics = data.get("WorkoutStatistics", None)
        if workout_statistics is not None:
            if isinstance(workout_statistics, dict):
                self.statistics = [self._parse_workout_statistic(workout_statistics)]
            else:
                self.statistics = list(map(lambda m: self._parse_workout_statistic(m), workout_statistics))

        workout_route = data.get("WorkoutRoute", None)
        if workout_route is not None:
            self.route = self._parse_workout_route(workout_route)

        if self.distance is None or self.distance_unit is None:
            statistic = self.get_statistic(HK_RECORD_DISTANCE_WALKING_RUNNING)
            if statistic is not None:
                self.distance = statistic['sum'] if statistic['sum'] is not None else None
                self.distance_unit = statistic['unit'] if statistic['unit'] is not None else 'mi'

        if self.energy_burned is None or self.energy_burned_unit is None:
            statistic = self.get_statistic(HK_RECORD_ACTIVE_ENERGY_BURNED)
            if statistic is not None:
                self.energy_burned = statistic['sum'] if statistic['sum'] is not None else None
                self.energy_burned_unit = statistic['unit'] if statistic['unit'] is not None else 'Cal'

    def get_statistic(self, statistic_type):
        for s in self.statistics:
            if s['name'] == statistic_type:
                return s
        return None

    def get_event(self, event_type):
        for s in self.events:
            if s['name'] == event_type:
                return s
        return None

    def _parse_workout_event(self, data):
        return {
            'name': data.get(TYPE),
            'date': _parse_date(data.get(DATE)),
            'duration': _parse_float(data.get(DURATION)),
            'duration_unit': data.get(DURATION_UNIT),
        }

    def _parse_workout_statistic(self, data):
        statistic_type = "SUM" if data.get(SUM, None) is not None else "AVG"
        return {
            'name': data.get(TYPE),
            'type': statistic_type,
            'start_date': _parse_date(data.get(START_DATE, None)),
            'end_date': _parse_date(data.get(END_DATE, None)),
            'sum': _parse_float(data.get(SUM, None)),
            'average': _parse_float(data.get(AVG, None)),
            'min': _parse_float(data.get(MIN, None)),
            'max': _parse_float(data.get(MAX, None)),
            'unit': _parse_float(data.get(UNIT, None)),
        }

    def _parse_workout_route(self, data):
        file_reference = data.get("FileReference", None)
        file_path = file_reference.get("@path", None)
        metadata = data.get("MetadataEntry", None)
        if metadata is None:
            metadata = []
        elif isinstance(metadata, dict):
            metadata = [self._parse_metadata(metadata)]
        elif isinstance(metadata, list):
            metadata = list(map(lambda m: self._parse_metadata(m), metadata))

        return {
            'file_path': file_path,
            'file_name': file_path.split("/")[-1],
            'metadata': metadata,
        }
