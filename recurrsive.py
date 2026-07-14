# num=int(input("enter the number"))
# factorial=1
# for i in range(1,num+1):
#     factorial=factorial*i
#     print(f"factorial of {i} is {factorial}")

def fact_rec(num):
    if num == 1:
        return 1
    else:
        factorial=num*fact_rec(num-1)
        return factorial


print(fact_rec(5))