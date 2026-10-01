# Fill out the code to make a very simple calculator

# ask the user to enter number1:

try:
    num1 = int(input("Enter the first number: "))

    # ask the user to enter number 2:
    num2 = int(input("Enter the second number: "))

    # calculate the result of adding those numbers together
    result = num1 + num2

    # print out the answer
    print(f"The sum is: {result}")
except:
    print("enter only numbers...")
