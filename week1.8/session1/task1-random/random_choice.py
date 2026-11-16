import random

# Read names from a file

with open("names.txt") as infile:
    names = [ line.strip() for line in infile ]

# Ask user to enter a number, then randomly choose that many names
# from the list, avoiding any duplicate choices

num = int(input("Enter a number: "))

for i in range(0, num):
    namesOut = names
    nextName = namesOut[random.randint(0, len(namesOut))]
    print(nextName)
    namesOut.remove(nextName)

# Display the chosen names, one per line
