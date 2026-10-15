# Week 1.3, Session 2: Word Counter

# We want to read in a text file, and calculate how many words are in it. 
# You can use any of the .txt files to test this - or even make your own.

# open and read the file

# calculate the number of words
# hint: you could use .split() to break up by spaces
# hint: watch out for empty lines that might give you empty strings

# display the wordcount

# Here are the word counts you should get:
# story.txt - 290
# story2.txt - 326
# glasses.txt - 210

newFile = True

while (newFile):
    print("WORD COUNTER")

    name = input("Enter file name (with extension): ")

    while (name != "glasses.txt" and name != "story.txt" and name != "story2.txt"):
        name = input("Invalid file name, try again: ")


    with open(name, "r") as file:
        content = file.read()

        words = content.split(" ")

        print("WORDS:", len(words))


    if (input("Press [N] for a new file word count: ").lower() == "n"):  
        newFile = True
    else:
        newFile = False
