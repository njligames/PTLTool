
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
*Question Thread*
 Please post any questions in this designated thread.

*Weekly Hourly Goal*
 Aim for 15 hours per week.
  of the past 5 weeks must be at least 15 hours.
  Time bracket: Monday 12:00 AM PST to Sunday 11:59 PM PST.

*Calculation Details*
 Platinum 15 hour window: 12AM PST Monday - 11:59PM PST Sunday
 Pay Period window: 4PM PST Monday - 3:59PM PST Monday
 Daily Post window: Yestarday's hours

*Incentives and Absences*
 Look out for spot monetary incentives.
 If you are going to be out, update your slack name example: James F - OOO (01-01-2024 to 01-02-2024)

*Task Approach*
 Do not make the same misake twice.
 Be proactive in task completion.
 Join project channels and identify project managers.
 Always be in the coders channels; if not, message for assistance. (#platinum-coders-team or platinum-coders-team)
 Save task IDs for reference in case of issues.
 Take screenshots in case of task-related problems.
 Make sure you have access to the resources you need.

*Documentation*
 [Flamingo Multiturn Deviations](https://canary.remotasks.com/en/instruction/657e07549d4d60ede9570c86?assignmentId=65dfc52038478c6b7c5bff79)
 [Flamingo Coders Tasker Support Doc](https://docs.google.com/document/d/1MYpMBfSKvfwyC-M7pHcL3vDVm71k3aY_qd7e3Tsh-0U/edit#heading=h.8dhaa6pwxwi2)
 [Bulba ICE Query Gen](https://docs.google.com/document/d/1JgLaZPd_NidvUCV6PtbyvftKkHryeaJAfyKQnRi4o7E/edit#heading=h.bdoi01yxv521)
 [Bulba ICE Query Gen FAQs](https://docs.google.com/document/d/e/2PACX-1vQW4pQBBazfNjc6plxlXu-VezbVEh7q8Jsk6Bn8fxUqEmSH5AWoSkAyRhirPeDjBae95Y5TQqO2vWTB/pub)
 [Bulba Code Eval Rating Chat Task](https://www.remotasks.com/en/instruction/65ce92c3baf2ed0704043740?assignmentId=65ea7b05f306b0e8d119d352)
 [Bulba Multiturn Split](https://www.remotasks.com/en/instruction/65dfb2aecfa617c7f98b9002?assignmentId=65e9b7648f5ef600c223ab33)

*Questions (TLDR; ask in the project channels FIRST)*
 Please search for the answers in the Platinum Coders Channel (#platinum-coders-team) or the Project Specific Channels.
  Channels
   Platinum Coders Channel
    #platinum-coders-team or platinum-coders-team
   Flamingo
    #platinum_flamingo_coder_onboarding or platinum_flamingo_coder_onboarding
    #flamingo_coding_general or flamingo_coding_general
    #flamingo_coding_platinum_general or flamingo_coding_platinum_general
   Vertigo
    #vertigo_coding_bigquery  or vertigo_coding_bigquery
    #vertigo_coding_bigquery_reviewers  or vertigo_coding_bigquery_reviewers
    #vertigo_coding_bq_translation or vertigo_coding_bq_translation
    #vertigo_coding_cif_evals or vertigo_coding_cif_evals
    #vertigo_coding_cif_evals_reviewers or vertigo_coding_cif_evals_reviewers
    #vertigo_coding_text_to_sql or vertigo_coding_text_to_sql
   Bulba
    #bulba_multiturn_general or bulba_multiturn_general
    #bulba-code-eval-rating-chat-tasks or bulba-code-eval-rating-chat-tasks
    #bulba_code_eval_chat_tasks_t_3 or bulba_code_eval_chat_tasks_t_3
    #bulba_code_gen_e2e-sft_platinum or bulba_code_gen_e2e-sft_platinum
    #bulba_ice_query_gen_attempters or bulba_ice_query_gen_attempters
   Bee
    #bee_coding_group_announcements or bee_coding_group_announcements
   POD channel
    #cplatr_james_pod or Cplatr_james_pod
 Please look at the Bookmarked and Pinned pages in the channels.
  Public type questions - Questions that other people would be benefit from the answers...
   Project specific questions
   Task specific questions
  Private type questions - Questions that could be considered private information.
   Pay questions
  When you message me for help, please format it as follows:
```
Remotask ID:
Project Name:
Description: (in under 20 words)
Ticket Number:
```

*Issue Resolution*
 For pay, EQ, tasks, or project issues:
  1. Gather information.
  2. Check with peers for similar experiences.
  3. If it is project/task specific question, there are at least four channels you can ask the question from your peers.
   Our public channel (#cplatr_james_pod )
   Platinum coders channel (#platinum-coders-team)
   Project channel(s) - Please tag me.
  4. If you issue goes unresolved, please submit a Support Ticket (Zendesk)
   How to:
    Remotasks: https://www.loom.com/share/f835796648044ed784df8bc939050cd1?sid=958d172e-1ea6-4a55-942c-435c7e893f90
    Outlier: https://www.loom.com/share/c298cffa4f8740409de93f8ddcee1b14

*Requests*
 Remotasks are now honoring their promise about the hour requirement. You must perform at least 15 hours for three of the past five weeks. If you do not do this, they will demote you from platinum.

*Office Hours*
    Flamingo Open Office
    Weekdays· 4:00 – 5:00pm EST
    Time zone: America/New_York
    Google Meet joining info
    Video call link: https://meet.google.com/wgm-iqvi-eyb
    Or dial: ‪(US) +1 470-771-2939‬ PIN: ‪706 528 376‬#
    More phone numbers: https://tel.meet/wgm-iqvi-eyb?pin=8835868116775
"""

names_string = "\nThese are the hours for yesterday...\n\n"
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

When you are in my Platinum POD, it is important to me that we act proactively so that we are ready when issues may arise.

When I joined the Platinum Team, I was presented with these four commitments.

The Four Commitments of a Winning Team
    1. Know your job
    2. Do what you’re asked
    3. Make people look good
    4. Look out for others

I think these four commitments will guide us to build a strong team!

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
# print(str(d))
try:
    filename="data/yesterday/" + str(d) + ".csv"
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

    os.system("export PATH=$PATH:/Applications/DiffMerge.app/Contents/MacOS/")

    f = open("current.json", "w")
    f.write(json.dumps(current_names, sort_keys=True, indent=4))
    f.close()

    f = open("previous.json", "w")
    f.write(json.dumps(previous_names, sort_keys=True, indent=4))
    f.close()

    # os.system("diffmerge previous.json current.json")
    # os.system("rm previous.json")
    # os.system("rm current.json")
