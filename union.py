
#!/usr/local/bin/python3

import sys
import csv
import json

result=[]
if not sys.stdin.isatty():
    for line in sys.stdin:
        result.append(line.rstrip())

data_sets = []
for n in range(1, len(sys.argv)):
    data_sets.append(json.loads(n))

for data_set in data_sets:
    result = result + data_set

print(json.dumps(result))
