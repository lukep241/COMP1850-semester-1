# Worksheet 1.2: Task 2 Solution
from util import read_numbers
import sys
import statistics

numbers = read_numbers()

if (len(numbers) == 0):
    sys.exit("Error: no numbers provided")


print("Minimum =", min(numbers))
print("Maximum =", max(numbers))
print("Mean =", statistics.mean(numbers))


numbers.sort()
print("Median =", numbers[len(numbers) // 2])