import json
import streamlit as st
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta
from frontend.streamlit_controller import STYLE, get_week_dates
from frontend.overview.controller import display_daily_activity_summary, display_activity_summaries, display_activity_summaries

# Set Streamlit to wide mode
st.set_page_config(layout="wide")

@st.cache_data
def load_activity_summaries(file_path):
    with open(file_path, 'r') as f:
        return json.load(f)

if 'selected_date' not in st.session_state:
    st.session_state.selected_date = datetime.now().date()

if 'mode' not in st.session_state:
    st.session_state.mode = 'Daily'

# Function to get the date string for a given date
def get_date_str():
    if st.session_state.mode == 'Daily':
        return st.session_state.selected_date.strftime('%Y/%m/%d')
    elif st.session_state.mode == 'Weekly':
        week_dates = get_week_dates(st.session_state.selected_date)
        return f"{week_dates[0].strftime('%Y/%m/%d')} to {week_dates[-1].strftime('%Y/%m/%d')}"
    else:
        return st.session_state.selected_date.strftime("%B %Y")

# Function to get the previous and next dates
def increment_date(delta):
    if st.session_state.mode == 'Daily':
        st.session_state.selected_date += timedelta(days=delta)
    elif st.session_state.mode == 'Weekly':
        st.session_state.selected_date += timedelta(weeks=delta)
    else:
        st.session_state.selected_date += relativedelta(months=delta)

def display_overview_tab(activity_summaries):
    st.subheader("Overview", anchor=False)
    # Example placeholder for sleep percentage visualization
    st.write("Overview data visualization will be here.")

def display_activity_tab(activity_summaries):
    st.subheader("Activity", anchor=False)
    if st.session_state.mode == 'Daily':
        display_daily_activity_summary(activity_summaries, st.session_state.selected_date)
    else:
        display_activity_summaries(activity_summaries, st.session_state.selected_date, st.session_state.mode)

def display_sleep_tab(activity_summaries):
    st.subheader("Sleep Percentage", anchor=False)
    # Example placeholder for sleep percentage visualization
    st.write("Sleep data visualization will be here.")

def display_exercise_tab(activity_summaries):
    st.subheader("Exercise Percentage", anchor=False)
    # Example placeholder for exercise percentage visualization
    st.write("Exercise data visualization will be here.")

def display_strain_tab(activity_summaries):
    st.subheader("Strain", anchor=False)
    # Example placeholder for activity percentage visualization
    st.write("Strain data visualization will be here.")

def main():
    st.markdown(STYLE, unsafe_allow_html=True)

    activity_summaries = load_activity_summaries("./data/processed/activity_summaries.json")
    st.session_state.mode = st.selectbox("Mode:", ['Daily', 'Weekly', 'Monthly'], label_visibility="hidden")

    # Navigation buttons
    col1, col2, col3 = st.columns([0.5, 1, 0.5])

    with col1:
        st.button("Previous", on_click=increment_date, args=(-1,))
    with col2:
        label = f"""{get_date_str()}"""
        st.write(label, unsafe_allow_html=True)
    with col3:
        st.button("Next", on_click=increment_date, args=(1,))

    # Tabs for different stats
    overview, tab1, tab2, tab3, tab4 = st.tabs(["Overview","Activity", "Sleep", "Exercise", "Strain"])
    with overview:
        display_overview_tab(activity_summaries)
    with tab1:
        display_activity_tab(activity_summaries)
    with tab2:
        display_sleep_tab(activity_summaries)
    with tab3:
        display_exercise_tab(activity_summaries)
    with tab4:
        display_strain_tab(activity_summaries)

if __name__ == "__main__":
    main()
