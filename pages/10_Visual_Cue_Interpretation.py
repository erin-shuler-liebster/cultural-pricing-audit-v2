# pages/10_Visual_Cue_Interpretation.py
import streamlit as st

st.title("📊 Pricing Visual Cue Interpretation Guide")
st.markdown("See how layout, color, and pricing structure map to Hofstede’s cultural dimensions.")

st.header("🖼️ Positioning")
st.markdown("""
- **Top-Left Pricing** → Aligns with **Low PDI** cultures (e.g., Sweden) → Egalitarian, transparent
- **Bottom-Right Pricing** → Better for **High PDI** cultures (e.g., India, Japan) → Respect authority flow
- **Centered Pricing** → Appeals broadly but especially in **high MAS** cultures → Dominant, assertive presence
""")

st.header("🎨 Color Psychology")
st.markdown("""
- **Red CTA Buttons** → Triggers urgency → Works well in **high UAI** and **MAS** cultures
- **Blue CTA Buttons** → Builds trust → Aligns with **high LTO** and **low MAS** (e.g., Sweden)
- **Gold/Premium** → Prestige signal for **high PDI** (Japan, India)
- **Green** → Ethical/eco cues → Appeals in **low MAS** and **high IVR** markets
""")

st.header("🏷️ Pricing Visual Features")
st.markdown("""
- **Strikethrough pricing (e.g., $120 → $85)** → Highly effective in **high UAI** cultures
- **“2 for 1” Bundles** → Best in **collectivist** contexts (India, Japan)
- **Countdown clocks / limited-time badges** → High **Indulgence** (USA, Mexico)
- **Trust Badges (SSL, reviews)** → Boost conversions in **high UAI** cultures (Japan, France)
""")

st.header("🌐 Strategic Usage")
st.markdown("""
Use this guide to:
- Design landing pages per country
- Choose pricing placements that feel **natural** per market
- Avoid layout structures that violate cultural expectations
""")
