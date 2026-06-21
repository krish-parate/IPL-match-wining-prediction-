import streamlit as st
import pandas as pd
import pickle

# Page Config
st.set_page_config(
    page_title="IPL Winning Prediction System",
    page_icon="",
    layout="wide"
)

# Load model and encoders
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

with open("encoders.pkl", "rb") as f:
    encoders = pickle.load(f)

# Title
st.title(" IPL Winning Prediction System")
st.markdown("### Predict the winner of an IPL match using Machine Learning")

# Teams List
teams = list(encoders["team1"].classes_)

# Two Columns
col1, col2 = st.columns(2)

with col1:
    team1 = st.selectbox(
        "Select Team 1",
        teams
    )

    toss_winner = st.selectbox(
        "Toss Winner",
        teams
    )

with col2:
    team2 = st.selectbox(
        "Select Team 2",
        teams
    )

    toss_decision = st.selectbox(
        "Toss Decision",
        ["bat", "field"]
    )

# Venue
venue = st.selectbox(
    "Venue",
    list(encoders["venue"].classes_)
)

# Prediction Button
if st.button(" Predict Winner"):

    if team1 == team2:
        st.error("Please select two different teams.")

    else:
        try:
            input_data = pd.DataFrame({
                "team1": [encoders["team1"].transform([team1])[0]],
                "team2": [encoders["team2"].transform([team2])[0]],
                "toss_winner": [encoders["toss_winner"].transform([toss_winner])[0]],
                "toss_decision": [encoders["toss_decision"].transform([toss_decision])[0]],
                "venue": [encoders["venue"].transform([venue])[0]]
            })

            prediction = model.predict(input_data)

            winner = encoders["winner"].inverse_transform(prediction)[0]

            st.success(f" Predicted Winner: {winner}")

        except Exception as e:
            st.error(f"Error: {e}")

# Footer
st.markdown("---")
st.markdown(
    "Built using Python, Streamlit, Pandas and Scikit-Learn"
)
