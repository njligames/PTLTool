
#!/usr/local/bin/python3

import sys
import csv
import json

stdin_emails=[]
for line in sys.stdin:
    stdin_emails.append(line.rstrip())

filename=None
if(len(sys.argv) > 1):
    filename=sys.argv[1]

if None != filename:
    pod_filename=filename
    pod_emails = stdin_emails
    try:
        with open(pod_filename) as csvfile:
            reader = csv.DictReader(csvfile)

            for row in reader:
                pod_emails.append(row["email"])

        print(json.dumps(pod_emails))
    except:
        print('file error', file=sys.stderr)
else:
    print(json.dumps(stdin_emails))
