fun=lambda a,b:a+b
a=int(input(f"please enter a: "))
b=int(input(f"please enter b: "))
res=fun(a,b)
print(res)

l1=[1,2,3,4,5,6,7,8,9]
even=lambda x:True if x%2==0 else False
filtered_ouput=filter(even,l1)
print(f'even numbs in the list are {list(filtered_ouput)}')

l1=[1,2,3,4,5,6,7,8,9]
even=lambda x:True if x%2==0 else False
mapped_ouput=map(even,l1)
print(f'mapping result of numbs(even:true) in the list are {list(mapped_ouput)}')