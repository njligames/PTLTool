
#!/usr/local/bin/python3

import sys
import csv
import json

def intersection(lst1, lst2):
    lst3 = [value for value in lst1 if value in lst2]
    return lst3

# Read from standard in
result=None
if not sys.stdin.isatty():
    result=[]
    for line in sys.stdin:
        result.append(line.rstrip())

# print("STANDARD IN")
# print(result)

# print("number of parameters " + str(len(sys.argv)))
# read from the parameters
data_sets = []
for n in range(1, len(sys.argv)):
    ary = json.loads(sys.argv[n])
    # print("param")
    # print(ary)
    data_sets.append(ary)

# print("PARAMETERS IN")
# print(data_sets)

if None == result:
    result = data_sets[0]

# create an intersection between standard in and each of the parameters
for data_set in data_sets:
    result = intersection(result, data_set)

# print("OUTPUT")
print(json.dumps(result))
