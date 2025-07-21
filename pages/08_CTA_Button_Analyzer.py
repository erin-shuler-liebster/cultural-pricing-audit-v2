# pages/01_CTA_Button_Analyzer.py
import streamlit as st
import re

st.title("CTA Button Analyzer")
st.markdown("Analyze CTA copy for tone, sentiment, and cultural alignment.")

cta_text = st.text_input("Paste CTA Button Text", value="Buy Now")

def analyze_cta(text):
    analysis = {}

    text = text.lower()

    # Sentiment tone
    if re.search(r"(buy|shop|order)", text):
        analysis["Tone"] = "💪 Masculine / Competitive"
    elif re.search(r"(explore|discover|learn)", text):
        analysis["Tone"] = "🧠 Low PDI / Informational"
    elif re.search(r"(custom|your|personal)", text):
        analysis["Tone"] = "👤 Individualistic"
    elif re.search(r"(group|family|shared)", text):
        analysis["Tone"] = "👥 Collectivistic"
    else:
        analysis["Tone"] = "🌀 Neutral or unclear"

    # Risk language
    if "guarantee" in text or "safe" in text:
        analysis["UAI alignment"] = "✅ Appeals to high uncertainty avoidance"
    else:
        analysis["UAI alignment"] = "⚠️ Might not reduce uncertainty"

    # Style hints
    if "now" in text:
        analysis["Urgency"] = "🚨 High urgency"
    else:
        analysis["Urgency"] = "🕒 Low urgency / soft call"

    return analysis

if st.button("Analyze CTA"):
    result = analyze_cta(cta_text)
    st.json(result)
