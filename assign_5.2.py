import re

num=list(range(1,11))

first_5=re.match(r'[0-9]{5}',num)

reversed_list=list(reversed(first_5))

print(f'Original list: {num}')
print(f'Extracted first five elements: {first_5}')
print(f'Reversed extracted elements: {reversed_list}')