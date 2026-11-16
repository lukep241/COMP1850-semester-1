import random

# Get user to input how many random numbers they want

# Generate this many random numbers

# Write the random numbers to a file named random.txt, one number per line

amount = int(input("Enter amount of random numbers to generate: "))

with open("random.txt", "w") as file:
    for i in range(amount):
        num = random.random()
        print(num)
        file.write(str(num)+"\n")
