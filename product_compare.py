# product_compare.py
from website_audit import audit_website

def compare_two_products(url1, url2, country, translator):
    tags1 = audit_website(url1)
    tags2 = audit_website(url2)

    score1 = translator.assess_alignment(tags1, country)
    score2 = translator.assess_alignment(tags2, country)

    return score1, score2
