# pdf_export.py
import pdfkit

def generate_report(data, filename="report.pdf"):
    html = "<h1>Cultural Pricing Report</h1>"
    for section, content in data.items():
        html += f"<h2>{section}</h2><p>{content}</p>"

    with open("temp.html", "w") as f:
        f.write(html)
    
    pdfkit.from_file("temp.html", filename)
    return filename
