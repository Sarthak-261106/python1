salary=float(input("Enter your salary: "))

if salary<0:
    raise ValueError("Salary cannot be negative")
else:
    print(f'your salary is {salary}')

#else we can use exception instead of specifying the error