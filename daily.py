
#!/usr/local/bin/python3

import os
import sys
import csv
import datetime
import json
from datetime import date
from datetime import datetime
from datetime import timedelta

def intersection(lst1, lst2):
    lst3 = [value for value in lst1 if value in lst2]
    return lst3

filename=None
if(len(sys.argv) > 1):
    filename=sys.argv[1]

if None == filename:
    print('file error', file=sys.stderr)
    exit(1)

def isNaN(num):
    return num != num

max_hours = 0
name_dict = {}
with open(filename) as csvfile:
    reader = csv.DictReader(csvfile)

    i = 0
    for row in reader:
        _hours = row["attemptHours"]
        if isNaN(_hours):
            hours = 0
        else:
            hours = float(_hours)

        name_dict[row["name"]] = {"hours":hours, "attempts":row["countAttempts"]}
        if hours > max_hours:
            max_hours = hours

name_dict_sorted = dict(sorted(name_dict.items()))

day_of_week = "{:%A}".format(date.today())
days_left = "zero days left"
if "Monday" == day_of_week:
    days_left = "six days left"
if "Tuesday" == day_of_week:
    days_left = "five days left"
if "Wednesday" == day_of_week:
    days_left = "four days left"
if "Thursday" == day_of_week:
    days_left = "three days left"
if "Friday" == day_of_week:
    days_left = "two days left"
if "Saturday" == day_of_week:
    days_left = "one day left"
if "Sunday" == day_of_week:
    days_left = "zero days left"

manager_string = "The project manager contacts are as follows:\n"
with open("data/PTL Platinum Project Directory - Coding.csv") as csvfile:
    reader = csv.DictReader(csvfile)

    indent = "\t\t"
    for row in reader:
        manager_string += indent + row["Project Name"] + " - " + row["Point of Contact"] + "\n"

top_message = """
:star2: Good day, Platinum Coders! :rocket:
Today is {}, {}
We have {} to hit our goals!!

""".format(day_of_week, date.today(), days_left)

top_message += """
* Question Thread:
   - Please post any questions in this designated thread.

* Weekly Hourly Goal:
   - Aim for 15 hours per week.
   - Time bracket: Monday 12:00 AM PST to Sunday 11:59 PM PST.

* Calculation Details:
    - Platinum 15 hour window: 12AM PST Monday - 11:59PM PST Sunday
    - Pay Period window: 4PM PST Monday - 3:59PM PST Monday

* Incentives and Absences:
   - Look out for spot monetary incentives.
   - If away, fill out the form with your Slack name marked as OOO (Out of Office).
   - [Out of Office Form](https://docs.google.com/forms/d/e/1FAIpQLSeZRLgRiliTMSLX4UGeZ79j0J7ms9P7A6M14VeBGd0_QjYgoQ/viewform)
   - Slack name example: James Folk - OOO (01-01-2024 to 01-02-2024)

* Task Approach:
   - Be proactive in task completion.
   - Join project channels and identify project managers.
   - Always be in the trial and coders channels; if not, message for assistance.
      - (#platinum-coders-trial or platinum-coders-trial)
      - (#platinum-coders-team or platinum-coders-team)
   - Save task IDs for reference in case of issues.
   - Take screenshots in case of task-related problems.

* Questions (TLDR; ask in the project channels FIRST)
    - Please search for the answers.
        - In the Platinum Coders Channel (#platinum-coders-team)
        - In the Platinum Trial Channel (#platinum-coders-trial)
        - In the Project Specifc Channels
            - Flamingo
                - #platinum_flamingo_coder_onboarding or platinum_flamingo_coder_onboarding
                - #flamingo_coding_general or flamingo_coding_general
                - #flamingo_coding_platinum_general or flamingo_coding_platinum_general
            - Vertigo
                - #vertigo_coding_bigquery  or vertigo_coding_bigquery
                - #vertigo_coding_bq_translation or vertigo_coding_bq_translation
                - #vertigo_coding_cif_evals or vertigo_coding_cif_evals
                - #vertigo_coding_cif_prompt or vertigo_coding_cif_prompt
                - #vertigo_coding_text_to_sql or vertigo_coding_text_to_sql
                - #vertigo-code-eval-prompt or vertigo-code-eval-prompt
        - In our POD channel (#cplatr_james_pod )
    - Please look at the Bookmarked and Pinned pages in the channels.
    - Public type questions - Questions that other people would be benefit from
        - Project specific questions
        - Task specific questions
    - Private type questions - Questions that could be considered private information
        - Can't make hours
        - Will be away
        - Pay questions
        - ect...
           - When you message me for help, please format it as follows:
                ```
                Remotask ID:
                Project Name:
                Description: (in under 20 words)
                Help/Escalation Ticket Number:
                ```
* Issue Resolution:
   - For pay, EQ, tasks, or project issues:
      1. Gather information.
      2. Check with peers for similar experiences.
      3. If it is project/task specific question, there are at least four channels you can ask the question from your peers.
        - Our public channel (#cplatr_james_pod )
        - Platinum coders channel (#platinum-coders-team)
        - Platinum trial channel (#platinum-coders-trial)
        - Project channel(s)
      4. After 2 hours, report issues through the escalation form: [Escalation Form](https://airtable.com/appE7bIarMItNVnpW/shrbz0F1YhqhfCRjx)
          - Indicate severity level:
             - Sev-2 Issue: Issue persisted for 2-5 hours.
             - Sev-1 Issue: Issue persisted for 5-8 hours.
             - Sev-0 Issue: Issue persisted for 8+ hours.
      5. For project/task issues, message the project manager in the project channel and tag me.
      6. For Sev-0 issues, direct message me with the Request Number.
      7. Escalation issues are monitored through AirTable.

* Requests:
   - If by the end of the week you feel that you cannot make your 15 hours, please private message me.
      1. Choose one of the Reasons:
         - Personal impediment
         - EQ issues
         - Technical Issues
         - New platinum
         - Other
      2. Format the message like this:
         ```
         Reason: (Personal impediment or EQ issues or Technical Issues or New platinum or Other)
         Detail: (in under 20 words)
         ```
      3. When you do this, it allows me to  better help you when you are audited by Remotasks.
"""

names_string = ""
for k, v in name_dict_sorted.items():
    name = k
    hour = float(v["hours"])
    attempt = int(v["attempts"])

    if hour >= 15.0:
        names_string += ":white_check_mark: "
    else:
        if hour == 0.0:
            names_string += ":rotating_light: "
        else:
            if isNaN(hour):
                names_string += ":construction: "
            else:
                names_string += ":warning: "

    names_string += "@" + name + " - " + str(round(hour, 2)) + " Hours with " + str(attempt) + " Attempts. "
    if max_hours == hour and 0.0 != hour:
        names_string += " :fire: :fire: :fire:\n"
    else:
        names_string += "\n"

bottom_message = """

As a Platinum Coder, we follow these three principles:
	1. Time - Minimum 15 hours
	2. Quality - 4/5 or 5/5 stars
	3. Communication - Please keep in contact with me.

When you are in my Platinum POD, it is important to me that we act proactivly so that we are ready when issues may arise.

When I joined the Platinum Team, I was presented with these four commitments.

The Four Commitments of a Winning Team
    1. Know your job
    2. Do what you’re asked
    3. Make people look good
    4. Look out for others

I think these four commitments will guide us to build a strong team!

 @James Folk - PTL
  :green_heart:

"""

message = top_message + names_string + bottom_message

print(message)

current_names = []
names_string = "This message is to make sure that my POD taskers are in the proper channels.\n"
i = 0
for k, v in name_dict_sorted.items():
    name = k
    current_names.append(name)
    names_string += "@" + name
    names_string += "\n"
    i += 1
    if i > 3:
        i = 0
        # print(names_string)
        names_string = "This message is to make sure that my POD taskers are in the proper channels.\n"
# print(names_string)


previous_names = []
now = datetime.now()
d = date(now.year, now.month, now.day)
d = d - timedelta(days=1)
try:
    filename="data/" + str(d) + ".csv"
    with open(filename) as csvfile:
        reader = csv.DictReader(csvfile)

        for row in reader:
            previous_names.append(row["name"])
except Exception as e:
    pass

modified = []

current_names.sort()
previous_names.sort()


# current_names.pop(0)
# current_names.insert(0,"HI")

for n in current_names:
    if n not in previous_names:
        modified.append(n)


# Use this command to add Diffmerge to the path
# export PATH=$PATH:/Applications/DiffMerge.app/Contents/MacOS/
if len(modified) > 0:

    f = open("current.json", "w")
    f.write(json.dumps(current_names, sort_keys=True, indent=4))
    f.close()

    f = open("previous.json", "w")
    f.write(json.dumps(previous_names, sort_keys=True, indent=4))
    f.close()

    os.system("diffmerge previous.json current.json")
    os.system("rm previous.json")
    os.system("rm current.json")
