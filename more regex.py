import re

s1='We are learning regex in python'
pat=r'[a-z]{3}'
match_obj=re.match(pat,s1)
print(match_obj)

phones='yaya-1234567890, yayaya-132547689'
pat=r'[0-9]{10}'
match_obj=re.findall(pat,phones)
print(match_obj)

phones='yaya-1234567890, yayaya-132547689'
pat=r'[0-9]{10}'
match_obj=re.finditer(pat,phones)
print(match_obj)

for match in match_obj:
    print(match)