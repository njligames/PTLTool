
#!/usr/local/bin/python3

import sys
import csv
import json

pod_filename=None
if(len(sys.argv) > 1):
    pod_filename=sys.argv[1]

audit_filename=None
if(len(sys.argv) > 2):
    audit_filename=sys.argv[2]

pod_emails = []
pod_slack = []

audit_emails = []
audit_thisweek = []
audit_lastweek = []
audit_2week = []
audit_3week = []
audit_4week = []
audit_color = []

try:
    # pod_filename="data/2024-02-05.csv"
    # with open(pod_filename) as csvfile:
    #     reader = csv.DictReader(csvfile)

    #     for row in reader:
    #         pod_emails.append(row["email"])
    #         pod_slack.append(row["name"])

    # audit_filename="data/Plat Reward - AB Test - Division.csv"
    with open(audit_filename) as csvfile:
        reader = csv.DictReader(csvfile)

        for row in reader:
            if "green".lower() != row["Robot"].lower() and "jamesf".lower() == row["PTL"].lower():
                audit_emails.append(row["WORKER_EMAIL"])
                audit_thisweek.append(row["This week"])
                audit_lastweek.append(row["Last week"])
                audit_2week.append(row["2 weeks ago"])
                audit_3week.append(row["3 weeks ago"])
                audit_4week.append(row["4 weeks ago"])
                audit_color.append(row["Robot"])

except Exception as e:
    print(e, file=sys.stderr)

for i in range(len(audit_emails)):
    # for i in range(len(pod_slack)):
    # if email == pod_emails[i]:
    print("*****************************************")
    message = "Hello, remotasks wanted me to let you know that you are in danger with not making your hours.\n"
    message += "Warning level from least to most: Green (safe), Yellow, Red, and Red Demotion (cannot help), you are " + audit_color[i] + "\n"
    message += audit_emails[i] + "\n"
    message += "Hours:\n"
    message += "\tThis week: " + audit_thisweek[i] + "\n"
    message += "\tLast week: " + audit_lastweek[i] + "\n"
    message += "\t2 weeks ago: " + audit_2week[i] + "\n"
    message += "\t3 weeks ago: " + audit_3week[i] + "\n"
    message += "\t4 weeks ago: " + audit_4week[i] + "\n"
    message += "You will be kept as a platinum tasker if you meet these three principles...\n"
    message += "\t1. Time - Minimum 15 hours\n"
    message += "\t2. Quality - 4/5 or 5/5 stars\n"
    message += "\t3. Communication - Communicate your project level issues with the project manager. Escalate your issues thorugh the escalation form (https://airtable.com/appE7bIarMItNVnpW/shrbz0F1YhqhfCRjx). Communicate with me if you have an empty queue.\n"

    print(message)

