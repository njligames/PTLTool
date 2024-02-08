

prompt = []

prompt.append("Expert(s) Email or Worker ID(s)")
prompt.append("Sev (0-2)")
prompt.append("Worker Team")
prompt.append("Issue Type: [EQ, Pay/Bonu, Technical Error, etc.]")
prompt.append("Issue Explanation")
prompt.append("Screenshots / Attachments")

ans = []
for i in [0, 1, 2, 3, 4]:
    ans.append(input(prompt[i] + ": "))

print("****************************\n\n")
i = 0
for a in ans:
    print(prompt[i] + ": " + a)
    i+=1
print("\n\n****************************")
