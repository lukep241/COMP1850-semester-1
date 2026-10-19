
def func_1(lst_value): 
    ''' 
    Takes a string of single-digit numbers
    Calculates the sum of the digits in the string
    Returns the sum divided by the amount of digits in the string
    ''' 

    sum = 0 
    num_of_value = len(lst_value) 
    for value in lst_value: 
        sum = sum + value 
    return sum/num_of_value 