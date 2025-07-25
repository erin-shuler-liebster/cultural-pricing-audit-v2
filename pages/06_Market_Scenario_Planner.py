# pages/06_Market_Scenario_Planner.py
import streamlit as st
import pandas as pd
from profiles import HOFSTEDE_PROFILES

st.title("Market Scenario Planner")
st.markdown("Compare predicted success across multiple cultural markets based on Hofstede 6-D model.")

selected_countries = st.multiselect(
    "Select Target Countries", list(HOFSTEDE_PROFILES.keys()), default=["Germany", "USA", "Japan"]
)

detected_tags = st.multiselect(
    "Detected Cultural Messaging Tags", ["power_distance", "individualism", "uncertainty_avoidance", "masculinity", "long_term_orientation", "indulgence"]
)

if st.button("Run Fit Simulation"):
    results = []
    for country in selected_countries:
        profile = HOFSTEDE_PROFILES[country]
        fit = {}
        for dim in profile:
            fit[dim] = "✅" if dim in detected_tags and profile[dim] > 0.5 else ("⚠️" if dim in detected_tags else "❌")
        results.append({"Country": country, **fit})

    df = pd.DataFrame(results)
    st.dataframe(df)
    st.download_button("📥 Download Scenario CSV", df.to_csv(index=False), file_name="market_scenario.csv")
