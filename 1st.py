print("Everything starts from 0")
print("Let's make a basic calculator")

x = int(input("Enter the first number: "))
y = int(input("Enter the second number: "))

def printing():
    print("Choose one of the follwing operations(1-4): ")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Divison")
    print("-1. Exit")

while True:
    printing()
    user_choice1 = int(input("Enter a choice from above options: "))
    if user_choice1 == 1:
        z = x + y
        print(f"The sum of the numbers is: {z}")
    elif user_choice1 == 2:
        z = x - y
        print(f"{x} - {y} is equal to {z}")
    elif user_choice1 == 3:
        z = x * y
        print(f"The product of {x} and {y} is {z}")
    elif user_choice1 == 4:
        if y == 0:
            print("Can't divide by zero")
        else:
            z = x / y
            print(f"{x} divided by {y} results in {z}")
    elif user_choice1 == -1:
        print("Exitting calculator")
        break
    else:
        print("Wrong input!!! try again!!")

print("Thank you for using our calculator.")