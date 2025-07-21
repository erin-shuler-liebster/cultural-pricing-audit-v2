# pages/08_Global_Hofstede_Map.py
import streamlit as st
import pandas as pd
from global_map import generate_hofstede_map

st.title("Global Hofstede Map")
st.markdown("Explore cultural dimensions across countries.")

df = pd.read_csv("hofstede_scores.csv")  # Preload CSV into repo
fig = generate_hofstede_map(df)
st.plotly_chart(fig)
