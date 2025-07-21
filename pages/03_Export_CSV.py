import streamlit as st
import pandas as pd
from website_audit import audit_website
from cultural_pricing_algorithm import CulturalPricingTranslator

profiles = {
    "USA": {"power_distance": 0.40, "individualism": 0.91, "uncertainty_avoidance": 0.46, "masculinity": 0.62, "long_term_orientation": 0.26, "indulgence": 0.68},
    "Germany": {"power_distance": 0.35, "individualism": 0.67, "uncertainty_avoidance": 0.65, "masculinity": 0.66, "long_term_orientation": 0.83, "indulgence": 0.40}
}

translator = CulturalPricingTranslator(profiles)

st.title("📤 Export Cultural Fit Report")

url = st.text_input("🔗 Enter URL to analyze")
country = st.selectbox("Select target market", list(profiles.keys()))

if st.button("Run Analysis"):
    tags = audit_website(url)
    feedback = translator.assess_alignment(tags, country)
    improvements = translator.recommend_improvements(tags, country)

    df = pd.DataFrame.from_dict(feedback, orient="index", columns=["Fit"])
    df["Improvement"] = df.index.map(improvements.get)

    st.dataframe(df)

    st.download_button("⬇️ Download CSV", data=df.to_csv(), file_name="cultural_audit.csv")
