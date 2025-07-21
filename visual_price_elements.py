# visual_price_elements.py
from bs4 import BeautifulSoup

def analyze_visual_pricing(html):
    soup = BeautifulSoup(html, 'html.parser')
    cues = {"color": [], "strikethrough": [], "sale_terms": []}

    for tag in soup.find_all(['span', 'div', 'p']):
        style = tag.get("style", "")
        text = tag.get_text(strip=True).lower()

        if "red" in style:
            cues["color"].append(("Red", text))
        if "line-through" in style or "<s>" in str(tag):
            cues["strikethrough"].append(text)
        if any(term in text for term in ["save", "off", "deal", "2 for 1", "%"]):
            cues["sale_terms"].append(text)

    return cues
