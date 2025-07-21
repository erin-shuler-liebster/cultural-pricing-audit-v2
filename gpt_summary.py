# gpt_summary.py
def summarize_cultural_alignment(feedback):
    summary = []
    for dim, note in feedback.items():
        if "✅" in note:
            summary.append(f"{dim.title()}: Strong match.")
        elif "⚠️" in note:
            summary.append(f"{dim.title()}: Moderate alignment. Review suggested.")
        else:
            summary.append(f"{dim.title()}: Potential cultural mismatch.")

    return "\n".join(summary[:5])  # Limit to top 5
