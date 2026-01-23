# Log Analyzer for Insider Threat Detection

An automated, rule-based security analysis system designed to detect insider threats by examining Linux authentication and system logs. The project combines structured log parsing, threat detection rules, risk scoring, and a web-based dashboard to provide fast, accurate, and actionable security insights.

## Introduction

Insider threats remain one of the most challenging security risks for organizations, as malicious or negligent users often have legitimate access to internal systems. Traditional security mechanisms primarily focus on external attackers and frequently overlook abnormal internal behavior.

This project addresses this gap by developing a lightweight and easily deployable log analysis system that automatically inspects Linux authentication logs (auth.log) to detect suspicious activities such as brute-force attempts, odd-hour access, and misuse of administrative privileges. The system assists security analysts in identifying high-risk users early and responding effectively.

## Objectives 

- To automate the analysis of Linux authentication logs
- To detect suspicious insider activities using rule-based detection
- To assign risk scores and prioritize users based on severity
- To present findings through an interactive and intuitive dashboard
- To generate structured reports for auditing and compliance

## System Features

Threat Detection Capabilities:
- Brute-Force Attack Detection
Identifies repeated failed login attempts within a short time window, indicating credential-guessing attacks.
- Odd-Hour Login Detection
Flags successful logins occurring outside predefined working hours, highlighting potential unauthorized access.
- Privilege Misuse Detection
Monitors excessive or unusual sudo command usage that may indicate privilege escalation attempts.

## Risk Scoring Mechanism

Each detected violation is assigned a predefined weight. A cumulative risk score is calculated per user, allowing:
- Classification of users into low, medium, and high-risk categories
- Prioritization of investigations based on severity

## Interactive Dashboard

The Streamlit-based dashboard provides:
- File upload via drag-and-drop
- Tabular views of suspicious users and risk scores
- Chronological timelines of events

## Automated Reporting

The system supports automatic generation of:
- CSV reports for integration with other security tools
- PDF reports for documentation and audits
- Excel reports for detailed analysis

Reports include:
- Executive summary
- User-wise risk analysis
- Event timelines
- Security recommendations

## Technologies Used

- Python – Core programming language
- Pandas – Log parsing and data analysis
- Streamlit – Interactive web dashboard
- Matplotlib – Data visualization
- FPDF / XlsxWriter – Report generation

## How to Run
Step 1: Clone the Repository
git clone https://github.com/your-username/log-analyzer-insider-threat.git
cd log-analyzer-insider-threat

Step 2: Install Dependencies
pip install -r requirements.txt

Step 3: Start the Dashboard
streamlit run src/dashboard.py

Step 4: Use the Application
- Open a browser and navigate to _http://127.0.0.1:8501_
- Upload a _.log_ or _.txt_ Linux authentication log file
- View detected threats, risk scores, and timelines
- Export reports as needed

## Performance and Benefits

- Rapid log analysis compared to manual inspection
- Reduced human error through automation
- Clear visualization of security events
- Suitable for small to medium-scale environments
- Minimal system resource requirements
