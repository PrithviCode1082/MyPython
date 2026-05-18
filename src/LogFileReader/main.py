#16
# Log File Analyser
# Parse a server log file (or generate sample data).
# Report: total requests, unique IPs, error rate (4xx/5xx), and peak hour.

times = []
def appender(text):
    text = text.split("- -")
    total = [txt for txt in text[1].split(" ") if txt != ""]
    ip = text[0]
    times.append(total[0])
    return {
        "IP Address": ip,
        "Time": total[0],
        "Request_Type": total[1],
        "Target": total[2],
        "Protocol": total[3],
        "Response": total[4]
    }


info = []

with open("server.log", 'r') as file:
    data = file.read().split("\n")
    for text in data:
        info.append(appender(text))

requests = 0
errors = 0
Unique_IPs = set()

for request in info:
    requests +=1
    Unique_IPs.add(request["IP Address"])
    if int(request["Response"]) > 200:
        errors += 1

print(f"Total Requests: {requests}")
print(f"Errors: {errors}")
print(f"Error Rate: {(errors / requests) * 100}%")
print("\nUnique IPs:")
[print(ip) for ip in Unique_IPs]
print()
print("Peak Hours: ")
peak_hours = {}
for time in times:
    if (time.split(":")[1]) in peak_hours:
        peak_hours[f"{time.split(":")[1]}"] += 1
    else:
        peak_hours[f"{time.split(":")[1]}"] = 1
        
[print(f"{k}:00 - {v} requests") for k, v in peak_hours.items()]
