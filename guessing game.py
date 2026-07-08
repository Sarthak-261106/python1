import random

print("Welcome to the number Guessing Game")
print('you hae 10 chances to guess')
print('the number should be less than 50')
number=random.randint(1,50)
for i in range(1,11):
    num = int(input("please guess a number"))
    if num>50:
        print('it should be less than 50')
    elif num>number:
        print('try lower')
    elif num<number:
        print('try higher')
    else:
        print('congratulation, you guessed the number')
        break

else:
    print('you lost')
    print(f'the number was {number}')
