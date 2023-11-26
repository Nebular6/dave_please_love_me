#Converts a positive number to a binary represented as a list of 0s and 1s.
#using the algorithm of divide by 2 and put the remainder in the small column then start again with the quotient as input
def pos_dec_to_binary(decimal,bit_list):
    if decimal<=1:
        bit_list.append(decimal%2)
        return list(reversed(bit_list))
    else:
        bit_list.append(decimal%2)
        return pos_dec_to_binary(decimal//2,bit_list)


#print(pos_dec_to_binary(1234,[]))