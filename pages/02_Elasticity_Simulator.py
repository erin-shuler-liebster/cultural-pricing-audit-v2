# pages/02_Elasticity_Simulator.py
import streamlit as st
import matplotlib.pyplot as plt
from elasticity_simulator import simulate_elasticity

st.title("Elasticity Simulator")
st.markdown("Estimate demand response to price changes in a specific cultural market.")

base_price = st.number_input("Base Price", value=100.0)
elasticity = st.slider("Elasticity Coefficient", 0.0, 2.0, 1.0)
culture_sensitivity = st.slider("Cultural Risk Factor", 0.1, 2.0, 1.0)

if st.button("Simulate"):
    prices, demand = simulate_elasticity(base_price, elasticity, culture_sensitivity)
    fig, ax = plt.subplots()
    ax.plot(prices, demand, marker='o')
    ax.set_xlabel("Price")
    ax.set_ylabel("Estimated Demand")
    st.pyplot(fig)
