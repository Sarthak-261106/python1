import re

message ="the current python version is 3.13. other versions are 3.12 ,3.11,3.10"

match_obj = re.search('13', message)
print(match_obj)

if re.search('yayy', message):
    print('Match found')
else:
    print('No match')