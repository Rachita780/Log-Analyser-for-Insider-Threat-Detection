from collections import defaultdict

def analyze_threats(events):
    threats = defaultdict(list)

    failed = defaultdict(int)
    sudo = defaultdict(int)

    for e in events:
        if e["event"] == "Failed Login":
            failed[e["user"]] += 1
        if e["event"] == "Privilege Usage":
            sudo[e["user"]] += 1

        if e["event"] == "Successful Login":
            hour = int(e["timestamp"].split()[2].split(":")[0])
            if hour < 6 or hour > 20:
                threats[e["user"]].append("Odd-hour login")

    for user, count in failed.items():
        if count >= 5:
            threats[user].append(f"Brute-force ({count} failures)")

    for user, count in sudo.items():
        if count >= 3:
            threats[user].append(f"Excessive sudo usage ({count} times)")

    return threats


if __name__ == "__main__":
    from log_collector import read_auth_log
    from log_parser import parse_logs

    threats = analyze_threats(parse_logs(read_auth_log()))
    print("Detected Threats:")
    for u, t in threats.items():
        print(u, "->", t)
