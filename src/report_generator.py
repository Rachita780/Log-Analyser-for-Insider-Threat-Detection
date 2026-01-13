from fpdf import FPDF
import pandas as pd
from datetime import datetime

from log_collector import read_auth_log
from log_parser import parse_logs
from threat_analyzer import analyze_threats
from risk_scoring import calculate_risk


def generate_pdf(threats, risks):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    # Title
    pdf.cell(0, 10, "Insider Threat Detection Report", ln=True)
    pdf.cell(0, 10, f"Generated on: {datetime.now()}", ln=True)
    pdf.ln(10)

    # Summary
    pdf.cell(0, 10, "Summary of Findings:", ln=True)
    pdf.ln(5)

    for user, issues in threats.items():
        pdf.cell(0, 10, f"User: {user}", ln=True)
        for issue in issues:
            pdf.cell(0, 10, f"- {issue}", ln=True)
        pdf.cell(0, 10, f"Risk Score: {risks[user]}", ln=True)
        pdf.ln(5)

    # Recommendations (ASCII ONLY)
    pdf.ln(5)
    pdf.cell(0, 10, "Recommendations:", ln=True)
    pdf.multi_cell(
        0, 8,
        "- Investigate high-risk users\n"
        "- Apply least privilege principle\n"
        "- Enable multi-factor authentication\n"
        "- Perform continuous monitoring of authentication logs\n"
        "- Conduct periodic security audits"
    )

    pdf.output("../reports/insider_threat_report.pdf")


def generate_excel(threats, risks):
    rows = []

    for user, issues in threats.items():
        rows.append({
            "User": user,
            "Threats": ", ".join(issues),
            "Risk Score": risks[user]
        })

    df = pd.DataFrame(rows)
    df.to_excel("../reports/insider_threat_report.xlsx", index=False)


if __name__ == "__main__":
    logs = read_auth_log()
    events = parse_logs(logs)
    threats = analyze_threats(events)
    risks = calculate_risk(threats)

    generate_pdf(threats, risks)
    generate_excel(threats, risks)

    print("PDF and Excel reports generated successfully.")
