import re

message ="The current Python version is 3.13. other versions are 3.12 ,3.11,3.10"

pat=r"[A-Z][a-z]{2,5}"
match_obj=re.search(pat,message)
print(match_obj)


# + one or more
pat=r"[A-Z][a-z]+"
match_obj=re.search(pat,message)
print(match_obj)


#? 0 or 1
pat=r"[A-Z][a-z]?"
match_obj=re.search(pat,message)
print(match_obj)


#* 0 or more
pat=r"[A-Z][a-z]*"
match_obj=re.search(pat,message)
print(match_obj)