import streamlit as st
import pandas as pd
from website_audit import audit_website
from cultural_pricing_algorithm import CulturalPricingTranslator

profiles = {
    "USA": {"power_distance": 0.40, "individualism": 0.91, "uncertainty_avoidance": 0.46, "masculinity": 0.62, "long_term_orientation": 0.26, "indulgence": 0.68},
    "Germany": {"power_distance": 0.35, "individualism": 0.67, "uncertainty_avoidance": 0.65, "masculinity": 0.66, "long_term_orientation": 0.83, "indulgence": 0.40},
    "France": {"power_distance": 0.68, "individualism": 0.71, "uncertainty_avoidance": 0.86, "masculinity": 0.43, "long_term_orientation": 0.63, "indulgence": 0.48},
    "Sweden": {"power_distance": 0.31, "individualism": 0.71, "uncertainty_avoidance": 0.29, "masculinity": 0.05, "long_term_orientation": 0.53, "indulgence": 0.78}
}

translator = CulturalPricingTranslator(profiles)

st.title("🌐 Cultural Comparison View")

url = st.text_input("🔗 Enter product page URL for cross-market testing")
countries = st.multiselect("Compare against these markets", list(profiles.keys()), default=["USA", "Germany"])

if st.button("Compare"):
    tags = audit_website(url)
    results = []

    for country in countries:
        feedback = translator.assess_alignment(tags, country)
        results.append({"Country": country, **feedback})

    df = pd.DataFrame(results).set_index("Country")
    st.dataframe(df)
