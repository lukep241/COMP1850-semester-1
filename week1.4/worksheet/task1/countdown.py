
def countdown(number): 
    '''  
    This recursive function takes a positive integer number  
    and counts the number down to zero printing each value. 
    ''' 
    
    try:
        if (number >= 0):
            print(number)       
            countdown(number-1) 
    except:
        print("Error. Input is not an integer")

