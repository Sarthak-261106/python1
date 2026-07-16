import re

s1 = 'Python is a programming language'

# ^ check only begin
pat=r"^[a-z]{8}"
match_obj=re.search(pat,s1)
print(match_obj)

#$ end
pat=r"[a-z]{8}$"
match_obj=re.search(pat,s1)
print(match_obj)

#group
email="abc123@xyz.com.edu"
pat=r"com|edu"
match_obj=re.search(pat,email)
print(match_obj)