import gspread
from datetime import datetime
import pytz

prompt = []

prompt.append("Expert(s) Email or Worker ID(s)")
prompt.append("Sev (0-2)")
prompt.append("Worker Team")
prompt.append("Issue Type: [EQ, Pay/Bonu, Technical Error, etc.]")
prompt.append("Issue Explanation")
prompt.append("Screenshots / Attachments")

ans = []
for i in [0, 1, 2, 3, 4, 5]:
    ans.append(input(prompt[i] + ": "))

def utcTime():
    local = pytz.timezone("America/Los_Angeles")
    naive = datetime.strptime("2001-2-3 10:11:12", "%Y-%m-%d %H:%M:%S")
    local_dt = local.localize(naive, is_dst=None)
    utc_dt = local_dt.astimezone(pytz.utc)
    return utc_dt.strftime("%Y-%m-%d %H:%M:%S")

sa = gspread.service_account(filename="service_account.json")
sheet = sa.open("PTL Issue Tracker")
worksheet = sheet.worksheet("PTL_ISSUES")


post = ""
i = 0
for a in ans:
    post += (prompt[i] + ": " + a) + "\n"
    i+=1

# TODO: add the post string to the body
body=[utcTime(), ans[0], ans[1], ans[2], ans[3], ans[4], ans[5], post]
worksheet.append_row(body, table_range="A1:J1")

print(post)
