from enum import Enum

## Characteristic Identifiers
class HKCharacteristicTypeIdentifier(str, Enum):
    ACTIVITY_MOVE_MODE = "@HKCharacteristicTypeIdentifierActivityMoveMode"
    DATE_OF_BIRTH = "@HKCharacteristicTypeIdentifierDateOfBirth"
    BIOLOGICAL_SEX = "@HKCharacteristicTypeIdentifierBiologicalSex"
    BLOOD_TYPE = "@HKCharacteristicTypeIdentifierBloodType"
    FITZPATRICK_SKIN_TYPE = "@HKCharacteristicTypeIdentifierFitzpatrickSkinType"
    WHEELCHAIR_USE = "@HKCharacteristicTypeIdentifierWheelchairUse"

    def __str__(self) -> str:
        return self.value

## Category Type Identifiers
class HKCategoryTypeIdentifierAppleStandHour(str, Enum):
    STOOD = "HKCategoryValueAppleStandHourStood"
    IDLE = "HKCategoryValueAppleStandHourIdle"

    def __str__(self) -> str:
        return self.value

class HKCategoryTypeIdentifierSleepAnalysis(str, Enum):
    IN_BED = "HKCategoryTypeIdentifierSleepAnalysisInBed"
    ASLEEP_UNSPECIFIED = "HKCategoryTypeIdentifierSleepAnalysisAsleepUnspecified"
    AWAKE = "HKCategoryTypeIdentifierSleepAnalysisAwake"
    ASLEEP_CORE = "HKCategoryTypeIdentifierSleepAnalysisAsleepCore"
    ASLEEP_DEEP = "HKCategoryTypeIdentifierSleepAnalysisAsleepDeep"
    ASLEEP_REM = "HKCategoryTypeIdentifierSleepAnalysisAsleepREM"

    def __str__(self) -> str:
        return self.value

HKCategoryTypeIdentifierAppleStandHourMapper = {
    HKCategoryTypeIdentifierAppleStandHour.STOOD: 0,
    HKCategoryTypeIdentifierAppleStandHour.IDLE : 1,
}


HKCategoryTypeIdentifierSleepAnalysisMapper = {
    HKCategoryTypeIdentifierSleepAnalysis.IN_BED: 0,
    HKCategoryTypeIdentifierSleepAnalysis.ASLEEP_UNSPECIFIED: 1,
    HKCategoryTypeIdentifierSleepAnalysis.AWAKE: 2,
    HKCategoryTypeIdentifierSleepAnalysis.ASLEEP_CORE: 3,
    HKCategoryTypeIdentifierSleepAnalysis.ASLEEP_DEEP: 4,
    HKCategoryTypeIdentifierSleepAnalysis.ASLEEP_REM: 5,

}

# ACTIVITY
class HKQuantityTypeIdentifierActivity(str, Enum):
    pass

# BODY MEASUREMENTS
class HKQuantityTypeIdentifierBodyMeasurements(str, Enum):
    BODY_MASS = "HKQuantityTypeIdentifierBodyMass"
    BODY_MASS_INDEX = "HKQuantityTypeIdentifierBodyMassIndex"
    LEAN_BODY_MASS = "HKQuantityTypeIdentifierLeanBodyMass"
    BODY_FAT_PERCENTAGE = "HKQuantityTypeIdentifierBodyFatPercentage"
    WAIST_CIRCUMFERENCE = "HKQuantityTypeIdentifierWaistCircumference"
    APPLE_SLEEPING_WRIST_TEMPERATURE = "HKQuantityTypeIdentifierAppleSleepingWristTemperature"

    def __str__(self) -> str:
        return self.value

# MOBILITY
class HKQuantityTypeIdentifierMobility(str, Enum):
    APPLE_WALKING_STEADINESS = "HKQuantityTypeIdentifierAppleWalkingSteadiness"
    SIX_MINUTE_WALK_TEST_DISTANCE =  "HKQuantityTypeIdentifierSixMinuteWalkTestDistance"
    WALKING_SPEED = "HKQuantityTypeIdentifierWalkingSpeed"
    WALKING_STEP_LENGTH = "HKQuantityTypeIdentifierWalkingStepLength"
    WALKING_ASYMMETRY_PERCENTAGE = "HKQuantityTypeIdentifierWalkingAsymmetryPercentage"
    WALKING_DOUBLE_SUPPORT_PERCENTAGE = "HKQuantityTypeIdentifierWalkingDoubleSupportPercentage"
    STAIR_ASCENT_SPEED = "HKQuantityTypeIdentifierStairAscentSpeed"
    STAIR_DESCENT_SPEED = "HKQuantityTypeIdentifierStairDescentSpeed"

    def __str__(self) -> str:
        return self.value

# DIETARY
class HKQuantityTypeIdentifierDietary(str, Enum):
    BIOTIN = "HKQuantityTypeIdentifierDietaryBiotin"
    CAFFEINE = "HKQuantityTypeIdentifierDietaryCaffeine"
    CALCIUM = "HKQuantityTypeIdentifierDietaryCalcium"
    CARBOHYDRATES = "HKQuantityTypeIdentifierDietaryCarbohydrates"
    CHLORIDE = "HKQuantityTypeIdentifierDietaryChloride"
    CHOLESTEROL = "HKQuantityTypeIdentifierDietaryCholesterol"
    CHROMIUM = "HKQuantityTypeIdentifierDietaryChromium"
    COPPER = "HKQuantityTypeIdentifierDietaryCopper"
    ENERGY_CONSUMED = "HKQuantityTypeIdentifierDietaryEnergyConsumed"
    FAT_MONOUNSATURATED = "HKQuantityTypeIdentifierDietaryFatMonounsaturated"
    FAT_POLYUNSATURATED = "HKQuantityTypeIdentifierDietaryFatPolyunsaturated"
    FAT_SATURATED = "HKQuantityTypeIdentifierDietaryFatSaturated"
    FAT_TOTAL = "HKQuantityTypeIdentifierDietaryFatTotal"
    FIBER = "HKQuantityTypeIdentifierDietaryFiber"
    FOLATE = "HKQuantityTypeIdentifierDietaryFolate"
    IODINE = "HKQuantityTypeIdentifierDietaryIodine"
    IRON = "HKQuantityTypeIdentifierDietaryIron"
    MAGNESIUM = "HKQuantityTypeIdentifierDietaryMagnesium"
    MANGANESE = "HKQuantityTypeIdentifierDietaryManganese"
    MOLYBDENUM = "HKQuantityTypeIdentifierDietaryMolybdenum"
    NIACIN = "HKQuantityTypeIdentifierDietaryNiacin"
    PANTOTHENIC_ACID = "HKQuantityTypeIdentifierDietaryPantothenicAcid"
    PHOSPHORUS = "HKQuantityTypeIdentifierDietaryPhosphorus"
    POTASSIUM = "HKQuantityTypeIdentifierDietaryPotassium"
    PROTEIN = "HKQuantityTypeIdentifierDietaryProtein"
    RIBOFLAVIN = "HKQuantityTypeIdentifierDietaryRiboflavin"
    SELENIUM = "HKQuantityTypeIdentifierDietarySelenium"
    SODIUM = "HKQuantityTypeIdentifierDietarySodium"
    SUGAR = "HKQuantityTypeIdentifierDietarySugar"
    THIAMIN = "HKQuantityTypeIdentifierDietaryThiamin"
    VITAMIN_A = "HKQuantityTypeIdentifierDietaryVitaminA"
    VITAMIN_B12 = "HKQuantityTypeIdentifierDietaryVitaminB12"
    VITAMIN_B6 = "HKQuantityTypeIdentifierDietaryVitaminB6"
    VITAMIN_C = "HKQuantityTypeIdentifierDietaryVitaminC"
    VITAMIN_D = "HKQuantityTypeIdentifierDietaryVitaminD"
    VITAMIN_E = "HKQuantityTypeIdentifierDietaryVitaminE"
    VITAMIN_K = "HKQuantityTypeIdentifierDietaryVitaminK"
    WATER = "HKQuantityTypeIdentifierDietaryWater"
    ZINC = "HKQuantityTypeIdentifierDietaryZinc"

    def __str__(self) -> str:
        return self.value

# WORKOUT TYPES
class HKWorkoutActivityType(str, Enum):
    AMERICAN_FOOTBALL = "HKWorkoutActivityTypeAmericanFootball"
    ARCHERY = "HKWorkoutActivityTypeArchery"
    AUSTRALIAN_FOOTBALL = "HKWorkoutActivityTypeAustralianFootball"
    BADMINTON = "HKWorkoutActivityTypeBadminton"
    BASEBALL = "HKWorkoutActivityTypeBaseball"
    BASKETBALL = "HKWorkoutActivityTypeBasketball"
    BOWLING = "HKWorkoutActivityTypeBowling"
    BOXING = "HKWorkoutActivityTypeBoxing"
    CLIMBING = "HKWorkoutActivityTypeClimbing"
    CRICKET = "HKWorkoutActivityTypeCricket"
    CROSS_TRAINING = "HKWorkoutActivityTypeCrossTraining"
    CURLING = "HKWorkoutActivityTypeCurling"
    CYCLING = "HKWorkoutActivityTypeCycling"
    DANCE = "HKWorkoutActivityTypeDance"
    DANCE_INSPIRED_TRAINING = "HKWorkoutActivityTypeDanceInspiredTraining"
    ELLIPTICAL = "HKWorkoutActivityTypeElliptical"
    EQUESTRIAN_SPORTS = "HKWorkoutActivityTypeEquestrianSports"
    FENCING = "HKWorkoutActivityTypeFencing"
    FISHING = "HKWorkoutActivityTypeFishing"
    FUNCTIONAL_STRENGTH_TRAINING = "HKWorkoutActivityTypeFunctionalStrengthTraining"
    GOLF = "HKWorkoutActivityTypeGolf"
    GYMNASTICS = "HKWorkoutActivityTypeGymnastics"
    HANDBALL = "HKWorkoutActivityTypeHandball"
    HIGH_INTENSITY_INTERVAL_TRAINING = "HKWorkoutActivityTypeHighIntensityIntervalTraining"
    HIKING = "HKWorkoutActivityTypeHiking"
    HOCKEY = "HKWorkoutActivityTypeHockey"
    HUNTING = "HKWorkoutActivityTypeHunting"
    LACROSSE = "HKWorkoutActivityTypeLacrosse"
    MARTIAL_ARTS = "HKWorkoutActivityTypeMartialArts"
    MIND_AND_BODY = "HKWorkoutActivityTypeMindAndBody"
    MIXED_METABOLIC_CARDIO_TRAINING = "HKWorkoutActivityTypeMixedMetabolicCardioTraining"
    OTHER = "HKWorkoutActivityTypeOther"
    PADDLE_SPORTS = "HKWorkoutActivityTypePaddleSports"
    PLAY = "HKWorkoutActivityTypePlay"
    PREPARATION_AND_RECOVERY = "HKWorkoutActivityTypePreparationAndRecovery"
    RACQUETBALL = "HKWorkoutActivityTypeRacquetball"
    ROWING = "HKWorkoutActivityTypeRowing"
    RUGBY = "HKWorkoutActivityTypeRugby"
    RUNNING = "HKWorkoutActivityTypeRunning"
    SAILING = "HKWorkoutActivityTypeSailing"
    SKATING_SPORTS = "HKWorkoutActivityTypeSkatingSports"
    SNOW_SPORTS = "HKWorkoutActivityTypeSnowSports"
    SOCCER = "HKWorkoutActivityTypeSoccer"
    SOFTBALL = "HKWorkoutActivityTypeSoftball"
    SQUASH = "HKWorkoutActivityTypeSquash"
    STAIR_CLIMBING = "HKWorkoutActivityTypeStairClimbing"
    SURFING_SPORTS = "HKWorkoutActivityTypeSurfingSports"
    SWIMMING = "HKWorkoutActivityTypeSwimming"
    TABLE_TENNIS = "HKWorkoutActivityTypeTableTennis"
    TENNIS = "HKWorkoutActivityTypeTennis"
    TRACK_AND_FIELD = "HKWorkoutActivityTypeTrackAndField"
    TRADITIONAL_STRENGTH_TRAINING = "HKWorkoutActivityTypeTraditionalStrengthTraining"
    VOLLEYBALL = "HKWorkoutActivityTypeVolleyball"
    WALKING = "HKWorkoutActivityTypeWalking"
    WATER_FITNESS = "HKWorkoutActivityTypeWaterFitness"
    WATER_POLO = "HKWorkoutActivityTypeWaterPolo"
    WATER_SPORTS = "HKWorkoutActivityTypeWaterSports"
    WRESTLING = "HKWorkoutActivityTypeWrestling"
    YOGA = "HKWorkoutActivityTypeYoga"

    def __str__(self) -> str:
        return self.value

# RECORD
HK_RECORD_ACTIVE_ENERGY_BURNED = "HKQuantityTypeIdentifierActiveEnergyBurned"
HK_RECORD_APPLE_EXERCISE_TIME = "HKQuantityTypeIdentifierAppleExerciseTime"
HK_RECORD_APPLE_STAND_TIME = "HKQuantityTypeIdentifierAppleStandTime"
HK_RECORD_AUDIO_EXPOSURE_EVENT = "HKCategoryTypeIdentifierAudioExposureEvent"
HK_RECORD_AUDIO_EXPOSURE_EVENT_LOUD_ENVIRONMENT = (
    "HKCategoryValueAudioExposureEventLoudEnvironment"
)
HK_RECORD_BASAL_BODY_TEMPERATURE = "HKQuantityTypeIdentifierBasalBodyTemperature"
HK_RECORD_BASAL_ENERGY_BURNED = "HKQuantityTypeIdentifierBasalEnergyBurned"
HK_RECORD_BLOOD_ALCOHOL_CONTENT = "HKQuantityTypeIdentifierBloodAlcoholContent"
HK_RECORD_BLOOD_GLUCOSE = "HKQuantityTypeIdentifierBloodGlucose"
HK_RECORD_BLOOD_PRESSURE_DIASTOLIC = "HKQuantityTypeIdentifierBloodPressureDiastolic"
HK_RECORD_BLOOD_PRESSURE_SYSTOLIC = "HKQuantityTypeIdentifierBloodPressureSystolic"
HK_RECORD_BODY_TEMPERATURE = "HKQuantityTypeIdentifierBodyTemperature"
HK_RECORD_CERVICAL_MUCUS_QUALITY_CREAMY = "HKCategoryValueCervicalMucusQualityCreamy"
HK_RECORD_CERVICAL_MUCUS_QUALITY_DRY = "HKCategoryValueCervicalMucusQualityDry"
HK_RECORD_CERVICAL_MUCUS_QUALITY_EGG_WHITE = (
    "HKCategoryValueCervicalMucusQualityEggWhite"
)
HK_RECORD_CERVICAL_MUCUS_QUALITY_STICKY = "HKCategoryValueCervicalMucusQualitySticky"
HK_RECORD_CERVICAL_MUCUS_QUALITY_WATERY = "HKCategoryValueCervicalMucusQualityWatery"

HK_RECORD_DISTANCE_CYCLING = "HKQuantityTypeIdentifierDistanceCycling"
HK_RECORD_DISTANCE_DOWNHILL_SNOW_SPORTS = (
    "HKQuantityTypeIdentifierDistanceDownhillSnowSports"
)
HK_RECORD_DISTANCE_SWIMMING = "HKQuantityTypeIdentifierDistanceSwimming"
HK_RECORD_DISTANCE_WALKING_RUNNING = "HKQuantityTypeIdentifierDistanceWalkingRunning"
HK_RECORD_DISTANCE_WHEELCHAIR = "HKQuantityTypeIdentifierDistanceWheelchair"
HK_RECORD_ELECTRODERMAL_ACTIVITY = "HKQuantityTypeIdentifierElectrodermalActivity"
HK_RECORD_ENVIRONMENTAL_AUDIO_EXPOSURE = (
    "HKQuantityTypeIdentifierEnvironmentalAudioExposure"
)
HK_RECORD_FLIGHTS_CLIMBED = "HKQuantityTypeIdentifierFlightsClimbed"
HK_RECORD_FORCED_EXPIRATORY_VOLUME1 = "HKQuantityTypeIdentifierForcedExpiratoryVolume1"
HK_RECORD_FORCED_VITAL_CAPACITY = "HKQuantityTypeIdentifierForcedVitalCapacity"
HK_RECORD_HANDWASHING_EVENT = "HKCategoryTypeIdentifierHandwashingEvent"
HK_RECORD_HEADPHONE_AUDIO_EXPOSURE = "HKQuantityTypeIdentifierHeadphoneAudioExposure"
HK_RECORD_HEART_RATE = "HKQuantityTypeIdentifierHeartRate"
HK_RECORD_HEART_RATE_VARIABILITY_S_D_N_N = (
    "HKQuantityTypeIdentifierHeartRateVariabilitySDNN"
)
HK_RECORD_HEIGHT = "HKQuantityTypeIdentifierHeight"
HK_RECORD_INHALER_USAGE = "HKQuantityTypeIdentifierInhalerUsage"
HK_RECORD_INSULIN_DELIVERY = "HKQuantityTypeIdentifierInsulinDelivery"
HK_RECORD_MINDFUL_SESSION = "HKCategoryTypeIdentifierMindfulSession"
HK_RECORD_NIKE_FUEL = "HKQuantityTypeIdentifierNikeFuel"
HK_RECORD_NOT_APPLICABLE = "HKCategoryValueNotApplicable"
HK_RECORD_NUMBER_OF_TIMES_FALLEN = "HKQuantityTypeIdentifierNumberOfTimesFallen"
HK_RECORD_OVULATION_TEST_RESULT_ESTROGEN_SURGE = (
    "HKCategoryValueOvulationTestResultEstrogenSurge"
)
HK_RECORD_OVULATION_TEST_RESULT_INDETERMINATE = (
    "HKCategoryValueOvulationTestResultIndeterminate"
)
HK_RECORD_OVULATION_TEST_RESULT_LUTEINIZING_HORMONE_SURGE = (
    "HKCategoryValueOvulationTestResultLuteinizingHormoneSurge"
)
HK_RECORD_OVULATION_TEST_RESULT_NEGATIVE = "HKCategoryValueOvulationTestResultNegative"
HK_RECORD_OXYGEN_SATURATION = "HKQuantityTypeIdentifierOxygenSaturation"
HK_RECORD_PEAK_EXPIRATORY_FLOW_RATE = "HKQuantityTypeIdentifierPeakExpiratoryFlowRate"
HK_RECORD_PERIPHERAL_PERFUSION_INDEX = (
    "HKQuantityTypeIdentifierPeripheralPerfusionIndex"
)
HK_RECORD_PUSH_COUNT = "HKQuantityTypeIdentifierPushCount"
HK_RECORD_RESPIRATORY_RATE = "HKQuantityTypeIdentifierRespiratoryRate"
HK_RECORD_RESTING_HEART_RATE = "HKQuantityTypeIdentifierRestingHeartRate"
HK_RECORD_RUNNING_STRIDE_LENGTH = "HKQuantityTypeIdentifierRunningStrideLength"
HK_RECORD_RUNNING_GROUND_CONTACT_TIME = "HKQuantityTypeIdentifierRunningGroundContactTime"
HK_RECORD_RUNNING_HEART_RATE_RECOVERY_ONE_MINUTE = "HKQuantityTypeIdentifierHeartRateRecoveryOneMinute"
HK_RECORD_RUNNING_POWER = "HKQuantityTypeIdentifierRunningPower"
HK_RECORD_RUNNING_SPEED = "HKQuantityTypeIdentifierRunningSpeed"
HK_RECORD_RUNNING_VERTICAL_OSCILLATION = "HKQuantityTypeIdentifierRunningVerticalOscillation"
HK_RECORD_SLEEP_DURATION_GOAL = "HKDataTypeSleepDurationGoal"
HK_RECORD_STEP_COUNT = "HKQuantityTypeIdentifierStepCount"
HK_RECORD_SWIMMING_STROKE_COUNT = "HKQuantityTypeIdentifierSwimmingStrokeCount"
HK_RECORD_TOOTHBRUSHING_EVENT = "HKCategoryTypeIdentifierToothbrushingEvent"
HK_RECORD_U_V_EXPOSURE = "HKQuantityTypeIdentifierUVExposure"
HK_RECORD_V_O2_MAX = "HKQuantityTypeIdentifierVO2Max"
HK_RECORD_WALKING_HEART_RATE_AVERAGE = "HKQuantityTypeIdentifierWalkingHeartRateAverage"

# ACTIVE SUMMARY
DATE_COMPONENTS = "@dateComponents"
ACTIVE_ENERGY_BURNED = "@activeEnergyBurned"
ACTIVE_ENERGY_BURNED_GOAL = "@activeEnergyBurnedGoal"
ACTIVE_ENERGY_BURNED_UNIT = "@activeEnergyBurnedUnit"
APPLE_EXERCISE_TIME = "@appleExerciseTime"
APPLE_EXERCISE_TIME_GOAL = "@appleExerciseTimeGoal"
APPLE_STAND_HOURS = "@appleStandHours"
APPLE_STAND_HOURS_GOAL = "@appleStandHoursGoal"

# METADATA
HK_AVERAGE_METS = "HKAverageMETs"
HK_ELEVATION_ASCENDED = "HKElevationAscended"
HK_INDOOR_WORKOUT = "HKIndoorWorkout"
HK_TIME_ZONE = "HKTimeZone"
HK_WEATHER_HUMIDITY = "HKWeatherHumidity"
HK_WEATHER_TEMPERATURE = "HKWeatherTemperature"
HK_WORKOUT_BRAND_NAME = "HKWorkoutBrandName"
HK_FOOD_MEAL = "HKFoodMeal"
HK_FOOD_TYPE = "HKFoodType"
HK_METADATA_KEY_HEART_RATE_MOTION_CONTEXT = "HKMetadataKeyHeartRateMotionContext"
HK_SWIMMING_STROKE_STYLE = "HKSwimmingStrokeStyle"

# WORKOUT
WORKOUT_ACTIVITY_TYPE = "@workoutActivityType"
DURATION = "@duration"
DURATION_UNIT = "@durationUnit"
TOTAL_DISTANCE = "@totalDistance"
TOTAL_DISTANCE_UNIT = "@totalDistanceUnit"
TOTAL_ENERGY_BURNED = "@totalEnergyBurned"
TOTAL_ENERGY_BURNED_UNIT = "@totalEnergyBurnedUnit"
TOTAL_FLIGHTS_CLIMBED = "@totalFlightsClimbed"
TOTAL_SWIMMING_STROKE_COUNT = "@totalSwimmingStrokeCount"

HK_CONSTANTS = {
    **HKCategoryTypeIdentifierAppleStandHourMapper,
    HK_RECORD_NOT_APPLICABLE: 0,
    HK_RECORD_AUDIO_EXPOSURE_EVENT_LOUD_ENVIRONMENT: 1,
    HK_RECORD_CERVICAL_MUCUS_QUALITY_DRY: 1,
    HK_RECORD_CERVICAL_MUCUS_QUALITY_STICKY: 2,
    HK_RECORD_CERVICAL_MUCUS_QUALITY_CREAMY: 3,
    HK_RECORD_CERVICAL_MUCUS_QUALITY_WATERY: 4,
    HK_RECORD_CERVICAL_MUCUS_QUALITY_EGG_WHITE: 5,
    HK_RECORD_OVULATION_TEST_RESULT_NEGATIVE: 1,
    HK_RECORD_OVULATION_TEST_RESULT_LUTEINIZING_HORMONE_SURGE: 2,
    HK_RECORD_OVULATION_TEST_RESULT_INDETERMINATE: 3,
    HK_RECORD_OVULATION_TEST_RESULT_ESTROGEN_SURGE: 4,
    **HKCategoryTypeIdentifierSleepAnalysisMapper,
}

TYPE = "@type"
SOURCE_NAME = "@sourceName"
SOURCE_VERSION = "@sourceVersion"
DEVICE = "@device"
CREATION_DATE = "@creationDate"
START_DATE = "@startDate"
END_DATE = "@endDate"
DATE = '@date'
UNIT = "@unit"
BPM = "@bpm"
TIME = "@time"

KEY = "@key"
VALUE = "@value"
MIN='@minimum'
MAX='@maximum'
AVG='@average'
SUM='@sum'



