# pages/05_AB_Hypothesis_Generator.py
import streamlit as st

st.title("A/B Test Hypothesis Generator (Cultural Model)")

st.markdown("Select a cultural dimension to see A/B test suggestions aligned to that value system.")

dimension = st.selectbox(
    "Choose Cultural Dimension",
    ["Power Distance", "Individualism", "Uncertainty Avoidance", "Masculinity", "LTO", "Indulgence"]
)

if st.button("Generate"):
    if dimension == "Power Distance":
        st.subheader("Power Distance (PDI)")
        st.write("A: 'Recommended by Experts'")
        st.write("B: 'Trusted by Our Community'")
    elif dimension == "Individualism":
        st.subheader("Individualism (IDV)")
        st.write("A: 'Your Personalized Plan'")
        st.write("B: 'Group Savings Offer'")
    elif dimension == "Uncertainty Avoidance":
        st.subheader("Uncertainty Avoidance (UAI)")
        st.write("A: '100% Money-back Guarantee'")
        st.write("B: 'Try It and See What Works'")
    elif dimension == "Masculinity":
        st.subheader("Masculinity (MAS)")
        st.write("A: 'Outperform Your Competitors'")
        st.write("B: 'Work-Life Balance Pricing'")
    elif dimension == "LTO":
        st.subheader("Long-Term Orientation (LTO)")
        st.write("A: 'Future-Proof Investment'")
        st.write("B: 'Quick and Easy Setup'")
    elif dimension == "Indulgence":
        st.subheader("Indulgence (IVR)")
        st.write("A: 'Treat Yourself Today'")
        st.write("B: 'Discipline Pays Off Later'")
