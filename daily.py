
#!/usr/local/bin/python3

import sys
import csv
from datetime import date

def intersection(lst1, lst2):
    lst3 = [value for value in lst1 if value in lst2]
    return lst3

# The name of the file that was exported by the Team Lead Dashboard
filename=None
if(len(sys.argv) > 1):
    filename=sys.argv[1]

if None == filename:
    print('file error', file=sys.stderr)
    exit(1)

pod_emails = []
pod_names = []
attemptHours = []
with open(filename) as csvfile:
    reader = csv.DictReader(csvfile)

    for row in reader:
        pod_emails.append(row["email"])
        pod_names.append(row["name"])
        attemptHours.append(row["attemptHours"])


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
""".format(date.today(), days_left)

def isNaN(num):
    return num != num

i = 0
hours=[]
for n in pod_names:
    _hour = attemptHours[i]
    try:
        hour = float(_hour)
    except:
        hour = float("nan")
    hours.append(hour)
    i = i + 1

m = max(hours)

i = 0
names_string = ""
for n in pod_names:
    _hour = attemptHours[i]
    try:
        hour = float(_hour)
    except:
        hour = float("nan")

    satisfied_hours = 15.0

    fraction = satisfied_hours / 6

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

    names_string += "@" + n + " - " + str(hour) + " Hours"
    if m == hour and 0.0 != hour:
        names_string += " :fire: :fire: :fire:\n"
    else:
        names_string += "\n"

    i = i + 1

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
Cheers to coding victories! :tada::sparkles:
@James Folk - PTL
 :green_heart:
"""

message = top_message + names_string + info_string

print(message)
