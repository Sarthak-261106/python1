import re

message ="the current python version is 3.13. other versions are 3.12 ,3.11,3.10"

match_obj = re.search('[0-9][0-9]', message)
print(match_obj)

#dot represent every characc if match dot [.]

 