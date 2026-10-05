# Worksheet 1.2: Task 2 Solution
from util import read_numbers
import sys

numbers = read_numbers()

if (len(numbers) == 0):
    sys.exit("Error: no numbers provided")


print("Minimum =", min(numbers))
print("Maximum =", max(numbers))
print("Mean =", sum(numbers) / len(numbers))


numbers.sort()

if (len(numbers) % 2 != 0): #if length of list is odd
    print("Median =", numbers[len(numbers) // 2])
else:
    mid = len(numbers) // 2
    median = (numbers[mid] + numbers[mid + 1]) / 2
    print("Median =", median)