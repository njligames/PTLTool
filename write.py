
#!/usr/local/bin/python3

import sys
import csv
import json


# Read from standard in
result=[]
if not sys.stdin.isatty():
    for line in sys.stdin:
        # print("RAW standard in")
        # print(line)
        if None != line:
            line = json.loads(line.rstrip())
            result = result + line

# print("STANDARD IN")
# print(result)

# read from the parameters
data_sets = []
for n in range(1, len(sys.argv)):
    ary = json.loads(sys.argv[n])
    data_sets.append(ary)

# print("PARAMETERS IN")
# print(data_sets)

# create an intersection between standard in and each of the parameters
for data_set in data_sets:
    result = result + data_set

# print("union")
# print(result)
for r in result:
    print(r)

