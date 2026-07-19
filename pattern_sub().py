import re

s1='Sunday,Monday,Tuesday,Wednesday,Thursday,Friday,Saturday,Sunday'
pat='Sunday'
replacement='Friday'

result=re.sub(pat,replacement,s1)
print(result)

result=re.sub(pat,replacement,s1,count=1)
print(result)