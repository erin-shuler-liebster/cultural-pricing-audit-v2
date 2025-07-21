# pages/01_CTA_Button_Audit.py
import streamlit as st
import requests
from cta_analyzer import analyze_cta_buttons

st.title("CTA Button Audit")
st.markdown("Analyze the tone, positioning, and styling of CTAs on your page.")

url = st.text_input("Enter product URL")

if url:
    html = requests.get(url, headers={"User-Agent": "Mozilla/5.0"}).text
    results = analyze_cta_buttons(html)
    
    st.subheader("Detected CTA Buttons")
    for res in results:
        st.markdown(f"- **Text**: {res['text']}  |  **Tone**: {res['tone']}")
