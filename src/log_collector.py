def read_auth_log(path="../logs/auth.log"):
    with open(path, "r") as file:
        return file.readlines()


if __name__ == "__main__":
    logs = read_auth_log()
    print("Total log lines:", len(logs))
    print("Sample log:")
    print(logs[0])
