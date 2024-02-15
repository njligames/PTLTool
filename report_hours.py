import csv
import datetime
from datetime import date

# I use this to see how my taskers do with hours by the end of the week.
# I am able to see this because I save the csv from the Team Lead Dashboard everyday

def totalHours(d):
    def isNaN(num):
        return num != num

    myData = {}

    weeks = 0
    loop = True
    while(loop):
        try:
            filename="data/" + str(d) + ".csv"
            with open(filename) as csvfile:
                print(filename)
                reader = csv.DictReader(csvfile)

                for row in reader:
                    _hours = row["attemptHours"]
                    if isNaN(_hours) or _hours == "":
                        hours = 0
                    else:
                        hours = float(_hours)

                    _attempts = row["countAttempts"]
                    if isNaN(_attempts):
                        attempts = 0
                    else:
                        attempts = int(_attempts)

                    if not row["name"] in myData.keys():
                        myData[row["name"]] = {"hours":hours, "attempts":attempts, "email":row["email"], "week":1}
                    else:
                        prevHours = myData[row["name"]]["hours"]
                        prevAttempts = myData[row["name"]]["attempts"]
                        prevWeek = myData[row["name"]]["week"]
                        myData[row["name"]] = {"hours":hours + prevHours, "attempts":attempts + prevAttempts, "email":row["email"], "week":prevWeek+1}

            d = d + datetime.timedelta(days=7)
            weeks += 1
        except Exception as e:
            loop = False
    return myData, weeks

hoursDict,weeks = totalHours(date(2024, 1, 20))
for k, v in hoursDict.items():
    if 0 == v["hours"]:
        message = k + " had zero hours with " + str(v["attempts"]) + " attempts (" + v["email"] + ")"
    elif 15 > (v["hours"] / weeks) and v["week"] >= 3:
        message = "@" + k + " had an average of " + str(v["hours"] / weeks) + " hours with " + str(v["attempts"]) + " attempts (" + v["email"] + ")"
        # message = "@" + k #+ " had an average of " + str(v["hours"] / weeks) + " hours with " + str(v["attempts"]) + " attempts (" + v["email"] + ")"
        print(message)
