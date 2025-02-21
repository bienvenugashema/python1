import re

with open("database.log", "r") as file:
    content = file.read()

ips = re.findall(r"(\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b)", content)

with open("filter_ips.txt", "a") as f:
    f.write(str(ips))
    


