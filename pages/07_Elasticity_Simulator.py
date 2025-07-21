# pages/02_Elasticity_Simulator.py
import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.title("Elasticity Simulator")
st.markdown("Understand how sensitive different markets are to price changes using basic elasticity modeling.")

base_price = st.number_input("Base Price (€)", value=100)
elasticity = st.slider("Elasticity Coefficient (e.g., -1.2 for Germany)", -3.0, 0.0, -1.2)
price_range = np.linspace(base_price * 0.5, base_price * 1.5, 20)
quantity_demanded = 1000 * (price_range / base_price) ** elasticity

st.subheader("Simulated Demand Curve")
fig, ax = plt.subplots()
ax.plot(price_range, quantity_demanded, color="green")
ax.set_xlabel("Price (€)")
ax.set_ylabel("Estimated Demand")
st.pyplot(fig)

st.markdown(f"**Interpretation**: A coefficient of `{elasticity}` means a 1% price increase leads to {abs(elasticity)}% drop in demand.")
st.markdown("You can adjust this by market — high UAI countries (Japan, France) tend to be more price-sensitive.")
