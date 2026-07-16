import re

s1 = 'python1 is a programing language'

pat=r"[a-z][a-z]"
match_obj=re.search(pat,s1)
print(match_obj)

#\d \D decimal capital oposite
pat=r"[a-z][a-z]\d"
match_obj=re.search(pat,s1)
print(match_obj)

pat=r"[a-z][a-z]\D"
match_obj=re.search(pat,s1)
print(match_obj)

#\s \S space or line break cap opposite
pat=r"[a-z]\s"
match_obj=re.search(pat,s1)
print(match_obj)

pat=r"[a-z]\S"
match_obj=re.search(pat,s1)
print(match_obj)

#\w matches [a-z] [A-Z] [0-9] \W oposite

