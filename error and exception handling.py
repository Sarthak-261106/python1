try:
    num1=int(input("Enter a number: "))
    num2=int(input("Enter another number: "))
    result = num1/num2
    print(result)
except ValueError:
    print("Invalid input")
except ZeroDivisionError:
    print("cannot divide by zero")
