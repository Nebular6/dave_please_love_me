#try to complete this
def factorial(input_number):
    if input_number <= 1:
        return 1            #base case
    else:
        return input_number * factorial(input_number-1)     #recursive case

print(factorial(4))            #this works and it fills me with smiles