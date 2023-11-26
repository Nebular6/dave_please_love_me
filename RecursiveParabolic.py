def is_palendromic(string):
    if len(string) <= 1:
        return "is palendromic"
    else:
        if string[0:1] == string[len(string)-1:len(string)]:
            return is_palendromic(string[1:-1])
        else:
            return "not palendromic"


testword = input("what word would you like to test: ")
print(is_palendromic(testword))


#if string == string[::-1]: #PS I KNOW YOU KNOW ABOUT THIS YOU LITTLE SHIT ITS SO MUCH BETTER THAN THIS RECURSION SHIT RAHHHHHHHH
#   return "True"
#else:
#   return "False" MORE EFFICIENT AND IT MAKES ME SMILE AND IT DIDNT TAKE 15 MINS TO FIGURE OUT 