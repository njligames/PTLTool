import csv
import datetime
from datetime import date
import json

def build(d, key, emptyValue):
    def isNaN(num):
        return num != num

    currentDate = d

    dates = []

    loop = True
    while(loop):
        try:
            filename="data/" + str(currentDate) + ".csv"
            with open(filename) as csvfile:
                reader = csv.DictReader(csvfile)

                dates.append(str(currentDate))

            currentDate = currentDate + datetime.timedelta(days=1)
        except Exception as e:
            loop = False

    currentDate = currentDate - datetime.timedelta(days=1)
    lastDate = currentDate

    myData = {}

    for date in dates:
        filename="data/" + date + ".csv"
        with open(filename) as csvfile:
            reader = csv.DictReader(csvfile)

            for row in reader:
                _key = emptyValue

                currentData = {str(d):_key}

                myData[row["name"]] = [currentData]

    dates = ["name"] + dates

    loop = True
    while(loop):
        try:
            filename="data/" + str(d) + ".csv"
            with open(filename) as csvfile:
                reader = csv.DictReader(csvfile)

                for row in reader:
                    _key = row[key]
                    if _key == "":_key=emptyValue

                    currentData = {str(d):_key}

                    if row["name"] in myData.keys():
                        myData[row["name"]].append(currentData)

            d = d + datetime.timedelta(days=1)
        except Exception as e:
            loop = False

    return myData, dates

def write(returnData, dates, key, emptyValue):
    with open('data/' + key + '.csv', 'w', newline='') as csvfile:
        fieldnames = dates
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for k, v in returnData.items():
            d = {'name':k}

            for date in dates:
                if date != "name":
                    d[date] = emptyValue

            for i in range(len(v)):
                for kk, vv in v[i].items():
                    d[kk] = vv

            writer.writerow(d)


def main():
    emptyValue = "0"
    key = "averageSpeedZScore"
    # key = "averageBmAccuracy"

    returnData, dates = build(date(2024, 1, 20), key, emptyValue)
    returnData_sorted = dict(sorted(returnData.items()))
    write(returnData_sorted, dates, key, emptyValue)

main()
