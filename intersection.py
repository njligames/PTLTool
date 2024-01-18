
#!/usr/local/bin/python3

import sys
import csv
import json

def intersection(lst1, lst2):
    lst3 = [value for value in lst1 if value in lst2]
    return lst3

result=[]
if not sys.stdin.isatty():
    for line in sys.stdin:
        result.append(line.rstrip())

data_sets = []
for n in range(1, len(sys.argv)):
    data_sets.append(json.loads(n))

for data_set in data_sets:
    result = intersection(result, data_set)

print(json.dumps(result))
