# streamlit_app.py
import streamlit as st
import pandas as pd
from cultural_pricing_algorithm import CulturalPricingTranslator
from website_audit import audit_website

# Cultural Profiles
profiles = {
    "USA": {"power_distance": 0.40, "individualism": 0.91, "uncertainty_avoidance": 0.46, "masculinity": 0.62, "long_term_orientation": 0.26, "indulgence": 0.68},
    "Germany": {"power_distance": 0.35, "individualism": 0.67, "uncertainty_avoidance": 0.65, "masculinity": 0.66, "long_term_orientation": 0.83, "indulgence": 0.40},
    "France": {"power_distance": 0.68, "individualism": 0.71, "uncertainty_avoidance": 0.86, "masculinity": 0.43, "long_term_orientation": 0.63, "indulgence": 0.48},
    "Sweden": {"power_distance": 0.31, "individualism": 0.71, "uncertainty_avoidance": 0.29, "masculinity": 0.05, "long_term_orientation": 0.53, "indulgence": 0.78}
}

translator = CulturalPricingTranslator(profiles)

st.set_page_config(layout="wide", page_title="🌍 Cultural Pricing Analyzer")
st.title("🌍 Cultural Pricing Communication Tool")
st.markdown("Analyze how your pricing strategy fits into global markets using Hofstede’s 6-D framework.")

url = st.text_input("🔗 Enter a product/sales page URL")
country = st.selectbox("🌐 Select target market", list(profiles.keys()))

if st.button("Analyze Cultural Fit"):
    with st.spinner("Auditing website..."):
        tags = audit_website(url)
        if "error" in tags:
            st.error("Website audit failed: " + tags["error"])
        else:
            st.subheader("📊 Cultural Signals Detected")
            st.json(tags)

            feedback = translator.assess_alignment(tags, country)
            improvements = translator.recommend_improvements(tags, country)

            st.subheader("✅ Fit Assessment")
            for dim, fb in feedback.items():
                st.markdown(f"**{dim.title()}**: {fb}")

            st.subheader("🛠️ Improvement Suggestions")
            for dim, note in improvements.items():
                st.markdown(f"- {note}")
