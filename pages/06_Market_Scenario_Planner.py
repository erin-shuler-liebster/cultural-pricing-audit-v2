# pages/06_Market_Scenario_Planner.py
import streamlit as st
import pandas as pd
from website_audit import audit_website
from cultural_pricing_algorithm import CulturalPricingTranslator
from profiles import HOFSTEDE_PROFILES

st.title("Market Scenario Planner")

url = st.text_input("URL to Analyze")
countries = st.multiselect("Select Markets to Simulate", list(HOFSTEDE_PROFILES.keys()))

translator = CulturalPricingTranslator(HOFSTEDE_PROFILES)

if st.button("Simulate Market Fit"):
    tags = audit_website(url)
    data = []
    for c in countries:
        feedback = translator.assess_alignment(tags, c)
        aligned = list(feedback.values()).count("✅ Matches cultural expectations")
        data.append({"Country": c, "Score": aligned})

    df = pd.DataFrame(data)
    st.bar_chart(df.set_index("Country"))
