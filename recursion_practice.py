import time

#Converts a positive number to a binary represented as a list of 0s and 1s.
#using the algorithm of divide by 2 and put the remainder in the small column then start again with the quotient as input
def pos_dec_to_binary(decimal,bit_list):
    if decimal<=1:
        bit_list.append(decimal%2)
        return list(reversed(bit_list))
    else:
        bit_list.append(decimal%2)
        return pos_dec_to_binary(decimal//2,bit_list)





#why does this not work? Fix it!
def countdown(number):
    if number <= 0:
        return number
    else:
        print(number)
        time.sleep(1)
        countdown(number-1)


#countdown(10)




#try to complete this
def fibonacci(n):
    if n == 0:#base case 1
        return 0
    elif n == 1:#base case 2
        return 1
    else:# recursive case
        return fibonacci(n-1) + fibonacci(n-2)

#for i in range(int(input(()))): # number inputted will be the nth term of the fibonachi returned
#    print(fibonacci(i))         #prints each time, looks nicer hehe



#triangular numbers
def triangular(n):
    if n <= 1:      #basec
        return 1
    else:           #recursed
        return n + triangular(n-1)


# print(triangular(4))          this works and it fills me with joy

#try to complete this
def factorial(input_number):
    if input_number <= 1:
        return 1            #base case
    else:
        return input_number * factorial(input_number-1)     #recursive case

#print(factorial(4))            #this works and it fills me with smiles




def is_palendromic(string):
    if len(string) <= 1:
        return "is palendromic"
    else:
        if string[0:1] == string[len(string)-1:len(string)]:
            return is_palendromic(string[1:-1])
        else:
            return "not palendromic"


#testword = ""  # dave this makes me want to die but i managerd to figure it out in the end, it actually made me think though
#print(is_palendromic(testword))
# PPS I DESERVE A HUG FOPR THIS 

#if string == string[::-1]: #PS I KNOW YOU KNOW ABOUT THIS YOU LITTLE SHIT ITS SO MUCH BETTER THAN THIS RECURSION SHIT RAHHHHHHHH
#   return "True"
#else:
#   return "False" MORE EFFICIENT AND IT MAKES ME SMILE AND IT DIDNT TAKE 15 MINS TO FIGURE OUT 


#try to complete a recursive linear search, returning the index of the item, or -1
def linear_search_recursive(items, search_item, n):
    n =+ 1
    if items[0] == search_item:
        return print("position ",n,)
    elif len(items) <= 0:
        return "false"
    else:
        x = len(items)
        return linear_search_recursive(items[1:x], search_item, n)

#print(linear_search_recursive([1,2,3,4,5,6,7,8,9],10,-1))


def binary_search_recursive(items, n, search_item):
    n=+1
    current_list_lenth=len(items)
    midway = round((current_list_lenth / 2))
    if items[midway] == search_item:
        return "in list"
    elif items[midway] < search_item:
        return binary_search_recursive(items[midway:], n, search_item)
    elif items[midway] < search_item:
        return binary_search_recursive(items[:midway], n, search_item)
    else:
        return "not in list sorry"



print(binary_search_recursive([1,2,3,4,5,6,7,8,9,10],-1,4))

#"""EXTENSION: Euclid's algorithm. The greatest common divisor (gcd) of two positive integers is the largest integer
#that divides evenly into both of them. For example, the gcd(102, 68) = 34.
#We can efficiently compute the gcd using the following property, which holds for positive integers p and q:

#If p > q, the gcd of p and q is the same as the gcd of q and p % q."""

#tests
#print(pos_dec_to_binary(1234,[]))
##or, neater (using a generator expression (outside scope of A-level CS))
#print("".join(str(i) for i in pos_dec_to_binary(1234,[])))
#
#print (factorial(4))
#print(binary_search_recursive([1,2,3,4,54,56,58],0,6,1))
#