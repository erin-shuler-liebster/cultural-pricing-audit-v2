# cta_analyzer.py
from bs4 import BeautifulSoup

def analyze_cta_buttons(html):
    soup = BeautifulSoup(html, 'html.parser')
    buttons = soup.find_all('a') + soup.find_all('button')
    
    ctas = []
    for btn in buttons:
        text = btn.get_text(strip=True).lower()
        styles = btn.get('style', '')
        result = {
            'text': text,
            'tone': classify_tone(text),
            'style': styles
        }
        ctas.append(result)
    return ctas

def classify_tone(text):
    if "buy" in text or "now" in text or "subscribe" in text:
        return "Directive / Masculine"
    elif "discover" in text or "your plan" in text:
        return "Collaborative / Feminine"
    elif "free" in text or "try" in text:
        return "Low commitment / Indulgent"
    else:
        return "Neutral or unclear"
