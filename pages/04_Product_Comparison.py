# pages/04_Product_Comparison.py
import streamlit as st
from website_audit import audit_website
from cultural_pricing_algorithm import CulturalPricingTranslator
from profiles import HOFSTEDE_PROFILES
from product_compare import compare_two_products

st.title("Compare Two Products by Market")

url1 = st.text_input("URL 1")
url2 = st.text_input("URL 2")
country = st.selectbox("Target Market", list(HOFSTEDE_PROFILES.keys()))

translator = CulturalPricingTranslator(HOFSTEDE_PROFILES)

if st.button("Compare"):
    feedback1, feedback2 = compare_two_products(url1, url2, country, translator)
    st.subheader("Product 1 Alignment")
    st.json(feedback1)
    st.subheader("Product 2 Alignment")
    st.json(feedback2)
