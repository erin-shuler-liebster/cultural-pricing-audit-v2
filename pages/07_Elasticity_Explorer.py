# pages/07_Elasticity_Explorer.py
import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.title("📈 Elasticity Explorer")

st.markdown("Simulate price sensitivity across different cultural contexts.")

country = st.selectbox("Select Country", ["USA", "Germany", "Japan", "India", "Sweden"])

base_price = st.slider("Base Price", 10, 1000, 100)
elasticity = st.slider("Price Elasticity (Negative)", -5.0, -0.1, -1.5)

# Cultural modifier per Hofstede UAI (risk avoidance)
cultural_modifier = {
    "USA": 0.9,
    "Germany": 0.95,
    "Japan": 0.5,
    "India": 0.7,
    "Sweden": 1.0,
}

modifier = cultural_modifier[country]

prices = np.linspace(base_price * 0.5, base_price * 1.5, 100)
demand = 1000 * (prices / base_price) ** elasticity * modifier

fig, ax = plt.subplots()
ax.plot(prices, demand, label="Demand Curve")
ax.set_xlabel("Price")
ax.set_ylabel("Expected Demand")
ax.set_title(f"Price Elasticity for {country}")
ax.grid(True)
st.pyplot(fig)

st.markdown(f"**Note:** Countries with high uncertainty avoidance (like Japan) show steeper demand drop-offs due to price change.")
