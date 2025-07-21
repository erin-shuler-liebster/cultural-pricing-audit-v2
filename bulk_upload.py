# bulk_upload.py
import pandas as pd
from website_audit import audit_website

def audit_csv(file, country, translator):
    df = pd.read_csv(file)
    results = []

    for url in df["URL"]:
        tags = audit_website(url)
        feedback = translator.assess_alignment(tags, country)
        improvements = translator.recommend_improvements(tags, country)
        results.append({
            "URL": url,
            "Feedback": feedback,
            "Improvements": improvements
        })

    return results
