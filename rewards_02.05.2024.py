
#!/usr/local/bin/python3

import sys
import csv
import json

pod_emails = []
pod_slack = []
reward_emails = []
try:
    pod_filename="data/2024-02-05.csv"
    with open(pod_filename) as csvfile:
        reader = csv.DictReader(csvfile)

        for row in reader:
            pod_emails.append(row["email"])
            pod_slack.append(row["name"])

    reward_filename="data/Plat Reward - AB Test - Division.csv"
    with open(reward_filename) as csvfile:
        reader = csv.DictReader(csvfile)

        for row in reader:
            if "c" != row["exp_group"].lower():
                reward_emails.append(row["EMAIL"])

except Exception as e:
    print(e, file=sys.stderr)

for email in reward_emails:
    for i in range(len(pod_slack)):
        if email == pod_emails[i]:
            print("@" + pod_slack[i])

