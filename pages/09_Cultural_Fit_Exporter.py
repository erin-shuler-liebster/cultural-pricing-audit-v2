# pages/09_Cultural_Fit_Exporter.py
import streamlit as st
import pandas as pd
from cultural_pricing_algorithm import CulturalPricingTranslator
from profiles import HOFSTEDE_PROFILES

st.title("Export Cultural Fit Recommendations")
st.markdown("Analyze cultural pricing fit across many countries.")

tags_input = st.multiselect("Detected Tags", ["power_distance", "individualism", "uncertainty_avoidance", "masculinity", "long_term_orientation", "indulgence"])

translator = CulturalPricingTranslator(HOFSTEDE_PROFILES)

rows = []
for country in HOFSTEDE_PROFILES:
    feedback = translator.assess_alignment({tag: True for tag in tags_input}, country)
    improvement = translator.recommend_improvements({tag: True for tag in tags_input}, country)
    rows.append({
        "Country": country,
        "Aligned Dimensions": ", ".join([k for k, v in feedback.items() if v.startswith("✅")]),
        "Suggested Improvements": "; ".join(improvement.values())
    })

df = pd.DataFrame(rows)
st.dataframe(df)
st.download_button("Download CSV", df.to_csv(index=False), file_name="cultural_fit_report.csv")
