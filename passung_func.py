def add_4(num):
    return num + 4

def square(num):
    return num * num

num=int((input("please enter a number: ")))
res=square(add_4(num))
print(f"after adding 4 to {num} the square of it is {res} ")