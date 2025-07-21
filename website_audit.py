# website_audit.py
import requests
from bs4 import BeautifulSoup
import re

def audit_website(url):
    try:
        headers = {"User-Agent": "Mozilla/5.0"}
        html = requests.get(url, headers=headers).text
        soup = BeautifulSoup(html, "html.parser")

        tags = {
            "power_distance": any(x in soup.text.lower() for x in ["exclusive", "premium", "experts"]),
            "individualism": any(x in soup.text.lower() for x in ["personalized", "just for you", "your"]),
            "uncertainty_avoidance": any(x in soup.text.lower() for x in ["guarantee", "secure", "no risk"]),
            "masculinity": any(x in soup.text.lower() for x in ["win", "best", "competition"]),
            "long_term_orientation": any(x in soup.text.lower() for x in ["sustainability", "investment", "future"]),
            "indulgence": any(x in soup.text.lower() for x in ["treat yourself", "deserve", "luxury"])
        }

        return tags
    except Exception as e:
        return {"error": str(e)}
