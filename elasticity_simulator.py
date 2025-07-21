# elasticity_simulator_tool.py
import numpy as np

def simulate_elasticity(base_price, elasticity, culture_sensitivity=1.0):
    prices = np.linspace(base_price * 0.5, base_price * 1.5, 10)
    demand = 100 * (1 - elasticity * ((prices - base_price) / base_price))
    
    adjusted_demand = demand * culture_sensitivity
    return prices, adjusted_demand
