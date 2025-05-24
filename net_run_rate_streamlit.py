# -*- coding: utf-8 -*-
"""
Created on Sat May 24 08:25:06 2025

@author: Glaston Jiue
"""

import streamlit as st

# Converts overs like 19.3 into actual float (e.g., 19.3 -> 19.5)
def convert_overs(overs_input):
    full_overs = int(overs_input)
    balls = round((overs_input - full_overs) * 10)
    if balls > 5:
        st.error("Invalid overs input: more than 6 balls in an over.")
        return 0
    return full_overs + (balls / 6)

# Calculate Net Run Rate
def calculate_nrr(runs, overs_faced, runs_conceded, overs_bowled):
    try:
        run_rate_scored = runs / overs_faced
        run_rate_conceded = runs_conceded / overs_bowled
        return round(run_rate_scored - run_rate_conceded, 2)
    except ZeroDivisionError:
        return "Invalid overs"

st.title("Cricket Net Run Rate (NRR) Calculator")

# Input fields
team1_name = st.text_input("Team 1 Name", "Team A")
team1_runs = st.number_input("Team 1 Runs", min_value=0)
team1_wickets = st.number_input("Team 1 Wickets", min_value=0, max_value=10)
team1_overs_raw = st.number_input("Team 1 Overs (e.g. 19.3)", min_value=0.0, step=0.1)

team2_name = st.text_input("Team 2 Name", "Team B")
team2_runs = st.number_input("Team 2 Runs", min_value=0)
team2_wickets = st.number_input("Team 2 Wickets", min_value=0, max_value=10)
team2_overs_raw = st.number_input("Team 2 Overs (e.g. 19.5)", min_value=0.0,  step=0.1)

default_overs = st.number_input("Default Overs (e.g. 20)", min_value=1.0, value=20.0, step=0.1)

if st.button("Submit"):
    team1_overs = convert_overs(team1_overs_raw)
    team2_overs = convert_overs(team2_overs_raw)

    # Adjust for teams all out before completing default overs
    actual_overs_team1 = min(team1_overs, default_overs) if team1_wickets < 10 else default_overs
    actual_overs_team2 = min(team2_overs, default_overs) if team2_wickets < 10 else default_overs

    nrr_team1 = calculate_nrr(team1_runs, actual_overs_team1, team2_runs, actual_overs_team2)
    nrr_team2 = calculate_nrr(team2_runs, actual_overs_team2, team1_runs, actual_overs_team1)

    st.markdown("### Results")
    st.write(f"{team1_name} Net Run Rate: `{nrr_team1}`")
    st.write(f"{team2_name} Net Run Rate: `{nrr_team2}`")

    
    

