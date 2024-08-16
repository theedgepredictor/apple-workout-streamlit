from datetime import datetime, timedelta
import streamlit as st
from dateutil.relativedelta import relativedelta
from statistics import mean
from frontend.streamlit_controller import get_week_dates
import plotly.graph_objects as go

def process_daily_summary(data):
    return {
        "active_energy_burned": data["active_energy_burned"],
        "exercise_time": data["exercise_time"],
        "stand_hours": data["stand_hours"],
    }

def process_summary(data):
    return {
        "total_active_energy_burned": round(sum(d["active_energy_burned"] for d in data),2),
        "avg_active_energy_burned": round(mean(d["active_energy_burned"] for d in data),2),
        "total_exercise_time": round(sum(d["exercise_time"] for d in data),2),
        "avg_exercise_time": round(mean(d["exercise_time"] for d in data),2),
        "total_stand_hours": round(sum(d["stand_hours"] for d in data),2),
        "avg_stand_hours": round(mean(d["stand_hours"] for d in data),2),
    }

def display_daily_activity_summary(activity_summaries, start_date: datetime):
    summary = activity_summaries.get(start_date.strftime('%Y-%m-%d'), {})
    if summary:
        st.write(f"Active Energy Burned: {summary.get('active_energy_burned', 'N/A')} {summary.get('active_energy_burned_unit', '')}")
        st.write(f"Active Energy Burned Goal: {summary.get('active_energy_burned_goal', 'N/A')} {summary.get('active_energy_burned_unit', '')}")
        st.write(f"Exercise Time: {summary.get('exercise_time', 'N/A')} min")
        st.write(f"Exercise Time Goal: {summary.get('exercise_time_goal', 'N/A')} min")
        st.write(f"Stand Hours: {summary.get('stand_hours', 'N/A')} hours")
        st.write(f"Stand Hours Goal: {summary.get('stand_hours_goal', 'N/A')} hours")
    else:
        st.write("No data available for this date.")

def display_activity_summaries(activity_summaries, start_date: datetime, mode):
    if mode == 'Monthly':
        month_start = start_date.replace(day=1)
        next_month_start = month_start + relativedelta(months=1)
        dates = [month_start + timedelta(days=i) for i in range((next_month_start - month_start).days)]
    else:
        dates = get_week_dates(start_date)

    active_energies = []
    exercise = []
    stand_hours = []
    monthly_data = []
    display_dates = []
    for date in dates:
        data = activity_summaries.get(date.strftime('%Y-%m-%d'), {})
        display_dates.append(date.strftime('%m/%d'))
        if data:
            monthly_data.append(data)
            active_energies.append(data['active_energy_burned'])
            exercise.append(data['exercise_time'])
            stand_hours.append(data['stand_hours'])
        else:
            active_energies.append([0])
            exercise.append([0])
            stand_hours.append([0])

    summary = process_summary(monthly_data)
    st.write(f"Total Active Energy Burned: {summary['total_active_energy_burned']} Cal")
    st.write(f"Average Active Energy Burned: {summary['avg_active_energy_burned']} Cal")

    fig = go.Figure()
    fig.add_trace(go.Bar(name='active_energy_plot', x=display_dates, y=active_energies, marker_color='red'))
    st.plotly_chart(fig, use_container_width=True)

    st.write(f"Total Exercise Time: {summary['total_exercise_time']} min")
    st.write(f"Average Exercise Time: {summary['avg_exercise_time']} min")

    fig = go.Figure()
    fig.add_trace(go.Bar(name='exercise_plot', x=display_dates, y=exercise, marker_color='green'))
    st.plotly_chart(fig, use_container_width=True)

    st.write(f"Total Stand Hours: {summary['total_stand_hours']} hours")
    st.write(f"Average Stand Hours: {summary['avg_stand_hours']} hours")

    fig = go.Figure()
    fig.add_trace(go.Bar(x=display_dates, y=stand_hours, marker_color='lightblue'))
    st.plotly_chart(fig, use_container_width=True)