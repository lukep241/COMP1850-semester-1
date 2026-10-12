# Worksheet 1.3: Task 1

L = int(input("Length of sequence: ")) # this should be your only input


# Your code for the Recaman Sequence
# You should store the sequence in an appropriate data structure named 'sequence'
sequence = [0]

for k in range(1, L):
    next_num = 0

    calc = sequence[k-1] - k
    if (calc < 0 or calc in sequence):
        calc = sequence[k-1] + k

    next_num = calc
    sequence.append(next_num)



# You may wish to use further output for testing purposes while you develop your code

[print(item) for item in sequence]    # this method is reasonably independent of the choice of data structure

# The web page https://en.wikipedia.org/wiki/Recam%C3%A1n%27s_sequence shows about 80 numbers in the sequence