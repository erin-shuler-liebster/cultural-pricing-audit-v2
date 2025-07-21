# global_map.py
import plotly.express as px
import pandas as pd

def generate_hofstede_map(hofstede_df):
    fig = px.choropleth(
        hofstede_df,
        locations="Country",
        locationmode="country names",
        color="Individualism",
        hover_name="Country",
        hover_data=["Power Distance", "Masculinity", "Uncertainty Avoidance", "LTO", "Indulgence"],
        title="Hofstede Cultural Dimensions (Interactive)"
    )
    return fig
