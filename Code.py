# Write a python function to print table of user input number :

def table():
    n = int(input("Enter a number to print the table:"))
    for i in range(1, 11):
        print(f"{n} * {i} = {n * i}")

table()