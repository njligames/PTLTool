
#!/usr/local/bin/python3

import sys
import csv
from datetime import date

def intersection(lst1, lst2):
    lst3 = [value for value in lst1 if value in lst2]
    return lst3

filename=None
if(len(sys.argv) > 1):
    filename=sys.argv[1]

if None == filename:
    print('file error', file=sys.stderr)
    exit(1)

name_dict = {}
with open(filename) as csvfile:
    reader = csv.DictReader(csvfile)

    i = 0
    for row in reader:
        name_dict[row["name"]] = {"hours":row["attemptHours"], "attempts":row["countAttempts"]}

name_dict_sorted = dict(sorted(name_dict.items()))

day_of_week = "{:%A}".format(date.today())
days_left = 0
if "Monday" == day_of_week:
    days_left = 5
if "Tuesday" == day_of_week:
    days_left = 4
if "Wednesday" == day_of_week:
    days_left = 3
if "Thursday" == day_of_week:
    days_left = 2
if "Friday" == day_of_week:
    days_left = 1
if "Saturday" == day_of_week:
    days_left = 0
if "Sunday" == day_of_week:
    days_left = 6

top_message = """
:star2: Good day, Platinum Coders! :rocket: Let’s Dive into Tech Awesomeness! Today is {}
Need a helping hand from our Platinum Technical Lead? :thinking_face: You’re in luck! Drop your questions in our daily help thread, and watch the magic happen! :sparkles:
We urge all team members to dedicate at least 15 hours per week, except for our exceptional interviewers. I’m delighted to announce that each member in our POD has not just met but surpassed this target. What a fantastic way to start the day, with such remarkable enthusiasm and dedication! Keep up the outstanding effort!

We’re all about that Platinum hustle, so we’re looking for folks who can kick butt and be present at least a bit each week. But hey, if life’s throwing curveballs your way and you need to dip out for personal reasons, hit up this form. Let the Platinum Ops Team know you’re still in the game but taking a timeout. We’re all in this together, superheroes! :muscle: #PlatinumLife #ResponsibilityCalls :male_superhero::female_superhero:

We have {} day left to hit our goals!!

When does the week start and end?
Start: Monday, 12:00 AM PST
End: Sunday, 11:59 PM PST

* This is the timeframe each expert has to meet the 15 hour tasking minimum each week.
* Each weeks Wednesday payout will reflect the total earned for tasks completed during this timeframe.

""".format(date.today(), days_left)

top_message += """
*If you need to go away, it would be helpful if you can update your slack name to show the dates.
EX: James Folk - OOO (01-01-2024 to 01-02-2024)

**********************************************************************************
These hours tend to be an overestimation. Please keep record of your own hours.
**********************************************************************************

"""

def isNaN(num):
    return num != num

m = max(hours)

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

    names_string += "@" + name + " - " + str(hour) + " Hours with " + str(attempt) + " Attempts. "
    if m == hour and 0.0 != hour:
        names_string += " :fire: :fire: :fire:\n"
    else:
        names_string += "\n"

info_string ="""
Information you need to include to expedite assistance:
* Remotask ID
* Task ID if applicable
* Email address
* Detailed description of problem/question/concern
* Screenshot/Screen-recording demonstrating the issue
:point_right: If our Platinum Technical Lead is on a coffee break, fret not! Post in the Platinum Coders channel
#platinum-coders-team (post-trial) or Platinum Coders Trial channel
#platinum-coders-trial (still on trial), and our brilliant community will swoop in to save the day! :male_superhero::female_superhero:
:female-technologist: Tell us your preferred project language with :star2: (https://forms.gle/cfYY4hCCDjWexCFo9) :star2:
:screwdriver: For issues with pay, tasks, projects, and EQ, fill out this :arrow_forward: (https://airtable.com/appE7bIarMItNVnpW/shrbz0F1YhqhfCRjx) :arrow_backward:. Here are the instructions. (https://airtable.com/appE7bIarMItNVnpW/shrbz0F1YhqhfCRjx)
Indicate the proper severity level:
\ta. Sev-2 Issue: The issue is new <2 hours
\tb. Sev-1 Issue: The issue has persisted for 2-5 hours
\tc. Sev-0 Issue: The issue has persisted for 5+ hours
But wait, there’s more! Use the daily chat thread to mingle, share insights, or throw some virtual high-fives. :handshake::speech_balloon:
:round_pushpin: Important links are right at the top for your swift navigation—because we’re all about efficiency! :zap:️
Need help? I’m just a message away! Let’s crush those code challenges together! :rocket::computer:
Tips...
If you are getting an error with a task, please message the admin of the project page for that task. It is important that you refer to the task number.
Cheers to coding victories! :tada::sparkles:

I would like to start a new habit.
If by the end of the week you feel that you cannot make your 15 hours, please private message me.
Choose one of the Reasons:
* Personal impediment
* EQ issues
* Technical Issues
* New platinum
* Other

Format it like this:
```
Reason: (Personal impediment or EQ issues or Technical Issues or New platinum or Other)
Detail: (in under 20 words)
```

When you do this, it allows me to  better help you when you are audited by Remotasks.

@James Folk - PTL
 :green_heart:
"""

message = top_message + names_string + info_string

print(message)
