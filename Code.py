# Write a python function to print table of user input number :

def table():
    n = int(input("Enter a number to print the table:"))
    for i in range(1, 11):
        print(f"{n} * {i} = {n * i}")

table()


# Write a python function to calculate average 3 User inputs

def average():
    num1 = float(input("Enter first number : "))
    num2 = float(input("Enter second number : "))
    num3 = float(input("Enter third number : "))

    total = num1 + num2 + num3
    avg = total / 3
    print(avg)
    
average()