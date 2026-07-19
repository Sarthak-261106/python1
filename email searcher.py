import re

with open('student_details','rt') as fh:
    data=fh.read()

pattern=r'[a-zA-Z0-9.-]+[@][a-z]+[.][a-z]'
match_obj=re.finditer(pattern,data)

for matches in match_obj:
    print(matches)