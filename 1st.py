print("Everything starts from 0")
print("Let's make a basic calculator")
x = int(input("Enter the first number: "))
y = int(input("Enter the second number: "))

print()

print("Choose one of the follwing operations(1-4): ")
print("1. Addition")
user_choice = int(input())
if user_choice == 1:
    z = x + y
    print(f"The sum of the numbers is: {z}")