import matplotlib.pyplot as plt
from risk_scoring import calculate_risk
from threat_analyzer import analyze_threats
from log_collector import read_auth_log
from log_parser import parse_logs

events = parse_logs(read_auth_log())
risks = calculate_risk(analyze_threats(events))

plt.bar(risks.keys(), risks.values())
plt.title("Risk Score per User")
plt.xlabel("User")
plt.ylabel("Risk Score")
plt.show()
