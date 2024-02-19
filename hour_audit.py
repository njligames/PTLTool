
#!/usr/local/bin/python3

import sys
import csv
import json

audit_filename=None
if(len(sys.argv) > 1):
    audit_filename=sys.argv[1]

audit_emails = []
audit_thisweek = []
audit_lastweek = []
audit_2week = []
audit_3week = []
audit_4week = []
audit_color = []

try:
    with open(audit_filename) as csvfile:
        reader = csv.DictReader(csvfile)

        for row in reader:
            if "james".lower() == row["PTL"].lower():
                audit_emails.append(row["WORKER_EMAIL"])
                audit_thisweek.append(row["This week"])
                audit_lastweek.append(row["Last week"])
                audit_2week.append(row["2 weeks ago"])
                audit_3week.append(row["3 weeks ago"])
                audit_4week.append(row["4 weeks ago"])
                audit_color.append(row["Robot"].lower())

except Exception as e:
    print(e, file=sys.stderr)

def textUpdate(color):
    message = ""
    if "green" == color:
        message = "You are completing your hours! :thumbsup:"
    elif "yellow" == color:
        message = "Remotasks wants me to contact you to improve your hours."
    elif "red" == color:
        message = "You are not meeting the expected hourly commitment. I will need you to message me why, so we can discuss."
    elif "red-demotion" == color:
        message = "I am unable to make an appeal for you. You will be demoted because of low hours."
    elif "magenta" == color:
        message = ""
    return message



for i in range(len(audit_emails)):
    print("*****************************************")
    message = "Hello! I have been given the weekly update for your hours." + "\n"
    message += textUpdate(audit_color[i].lower()) + "\n"
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
    message += "\t3. Communication - Please refer to the daily thread in our POD.\n"

    print(message)

# :medium-risk:How we can read the weekly hours report?:medium-risk:
# Green: The Platinum Experts are completing the hours! :thumbs:
# Yellow: We recommend to contact the Experts so they can improve their hours.
# Red: Please inform the Experts that they are not meeting the expected hourly commitment and provide specific comments about their overall performance.
# You can always appeal for someone, in that case they will appear as Red-Appeal (in case the appeal was accepted)
# Red-Demotion: There isn’t a possibility to appeal and demotion is imperative (0 hours in 5 weeks).
