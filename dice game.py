import random
print("Welcome to Dice Game")
while True:
    choice = input("Please press 'enter' to roll dice or 'q' to quit: ")
    choice=choice.strip()
    if choice == "q":
        print("Goodbye")
        break
    elif choice=='':
        number = random.randint(1,6)
        print("You rolled a ",number)
    else:
        print("Please enter a valid choice")

