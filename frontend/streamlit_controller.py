import json
from datetime import datetime, timedelta
import streamlit as st
from dateutil.relativedelta import relativedelta

WORKOUT_DICT = {
    "MONDAY": {"text": "Lower Body", "color": "red"},
    "TUESDAY": {"text": "Interval", "color": "yellow"},
    "WEDNESDAY": {"text": "Upper Body", "color": "blue"},
    "THURSDAY": {"text": "LISS", "color": "orange"},
    "FRIDAY": {"text": "Full Body", "color": "purple"},
    "SATURDAY": {"text": "Long Run", "color": "lime"},
    "SUNDAY": {"text": "Rest", "color": "green"},
}

STYLE = """
    <style>
        .stTabs [data-baseweb="tab-list"] {
            justify-content: center;
            text-align: center;
        }
        .stTabs [data-baseweb="tab"] {
            height: 50px;
            padding-top: 10px;
            padding-bottom: 10px;
            padding-left: 20px;
            padding-right: 20px;
            margin: 0 5px;
        }
        .stTabs [data-baseweb="tab"]:hover {
            background-color: #f0f0f0;
        }
    </style>
    <style>
        div[data-baseweb="tab-panel"] {
            justify-content: center;
            text-align: center;
        }
        div[class="plot-container plotly"] {
            justify-content: center;
            text-align: center;
        }
        div[data-testid="column"] {
            text-align: center;
        }
        div[data-testid="column"]:nth-of-type(1) {
            justify-content: left;
            padding-left: 20px;
        }
        div[data-testid="column"]:nth-of-type(2) {
            justify-content: center;
            text-align: center;
        }
        div[data-testid="column"]:nth-of-type(3) {
            justify-content: right;
            padding-right: 20px;
        }
        div[data-testid="stSelectbox"] {
            display: block;
            text-align: center;
            padding-right: 25%;
            padding-left: 25%
        }
        p {
            padding-bottom: 0px;
        }
    </style>
"""


def get_week_dates(start_date):
    start_of_week = start_date - timedelta(days=start_date.weekday())
    return [start_of_week + timedelta(days=i) for i in range(7)]

def process_calendar_events(activity_summaries):
    events = []
    for date_str in activity_summaries.keys():
        date = datetime.strptime(date_str, '%Y-%m-%d')
        date_dow = date.strftime('%A').upper()  # Get day of the week
        if date_dow in WORKOUT_DICT:
            events.append({
                "date": date_str,
                "title": WORKOUT_DICT[date_dow]['text'],
                "color": WORKOUT_DICT[date_dow]['color']
            })
    return events
