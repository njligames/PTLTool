
#!/usr/local/bin/python3

import sys
import csv
import json

result=[]
if not sys.stdin.isatty():
    for line in sys.stdin:
        result.append(line.rstrip())

filename=None
if(len(sys.argv) > 1):
    filename=sys.argv[1]

if None != filename:
    pod_filename=filename
    pod_names = []
    try:
        with open(pod_filename) as csvfile:
            reader = csv.DictReader(csvfile)


            for row in reader:
                for em in result:
                    if em == row["email"]:
                        pod_names.append("@" + row["name"] + " ")


        print(json.dumps(pod_names))
    except:
        print('file error', file=sys.stderr)
else:
    print(json.dumps(result))
