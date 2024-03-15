
#!/usr/local/bin/python3

import sys
import csv
import json
import operator
import datetime
from datetime import date
from datetime import datetime
from datetime import timedelta

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
audit_status = []

# WORKER_ID,WORKER_EMAIL,PLAT_STAT,This week,Last week,2 weeks ago,3 weeks ago,4 weeks ago,5 weeks ago,Average Hours,Robot,Status,TL,Start date,Z Score,NOTICE_2,NOTICE_3,CHEATING,CANNOT_BE_PLATINUM
try:
    with open(audit_filename) as csvfile:
        reader = csv.DictReader(csvfile)

        for row in reader:
            if "james".lower() == row["TL"].lower():
                audit_emails.append(row["WORKER_EMAIL"])
                audit_thisweek.append(row["This week"])
                audit_lastweek.append(row["Last week"])
                audit_2week.append(row["2 weeks ago"])
                audit_3week.append(row["3 weeks ago"])
                audit_4week.append(row["4 weeks ago"])
                audit_color.append(row["Robot"].lower())
                audit_status.append(row["Status"].lower())

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

def textStatus(status):
    message = ""

    if "on track" == status:
        message = "You are completing your hours! :thumbsup:\n"
    elif "off track" == status:
        message = "Remotasks wants me to contact you to improve your hours.\n"

    return message


name_dict = {}
for i in range(len(audit_emails)):
    print("\n*****************************************\n")
    message = "Hello! I have been given the weekly update for your hours." + "\n"
    message += textStatus(audit_status[i].lower())
    message += audit_emails[i] + "\n"
    message += "Hours:\n"
    message += "\tThis week: " + audit_thisweek[i] + "\n"
    message += "\tLast week: " + audit_lastweek[i] + "\n"
    message += "\t2 weeks ago: " + audit_2week[i] + "\n"
    message += "\t3 weeks ago: " + audit_3week[i] + "\n"
    message += "\t4 weeks ago: " + audit_4week[i] + "\n"
    message += "You will be kept as a platinum tasker if you meet these three principles...\n"
    message += "\t1. Time - Minimum 15 hours. (3 of the 5 weeks should be 15 hours or more)\n"
    message += "\t2. Quality - 4/5 or 5/5 stars\n"
    message += "\t3. Communication - Please refer to the daily thread in our POD.\n"
    message += "*** 3/5 weeks have to be 15 hours or more."

    name_dict[audit_emails[i]] = float(audit_lastweek[i])

    print(message)

cross_name_dict = {}
now = datetime.now()
d = date(now.year, now.month, now.day)
d = d - timedelta(days=1)
try:
    filename="data/yesterday/" + str(d) + ".csv"
    with open(filename) as csvfile:
        reader = csv.DictReader(csvfile)

        for row in reader:
            cross_name_dict[row["email"]] = row["name"]
except Exception as e:
    pass

message = "Leader Board\n"
message += "2/26/2023 to 3/3/2023" + "\n"

i = 1
for item in sorted(name_dict.items(), key=operator.itemgetter(1), reverse=True):
    email = item[0]
    hours = item[1]
    if email in cross_name_dict.keys():
        name = cross_name_dict[email]
    else:
        name = "N/A"

    message += "#" + str(i) + "\t@" + name + " with " + str(hours) + " hours\n"
    i += 1

print(message)
