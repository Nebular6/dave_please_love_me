#"""EXTENSION: Euclid's algorithm. The greatest common divisor (gcd) of two positive integers is the largest integer
#that divides evenly into both of them. For example, the gcd(102, 68) = 34.
#We can efficiently compute the gcd using the following property, which holds for positive integers p and q:
#If p > q, the gcd of p and q is the same as the gcd of q and p % q."""

def Divisors_of_a_number(number):
    Divisors_list = []
    for i in range(1,number):
        if number / i == round(number / i):
            Divisors_list.append(i)
        else:
            pass
    return Divisors_list #beautiful subroutine to return a list of numbers than evenly divide a whole number


def EuclidsAlgorithm(divisors_a, divisors_b): #i can be asked to comment this sorry future me jsut know im on some wizard shit rn
    AlreadySortedListBeacuseImIteratingFromLowToHighThisIsSoFuckingAss = []
    for a in range(0,len(divisors_a)):
            for b in range(0,len(divisors_b)):
                if divisors_a[a] ==divisors_b[b]:
                    AlreadySortedListBeacuseImIteratingFromLowToHighThisIsSoFuckingAss.append(divisors_a[a])
                else:
                    pass
    return AlreadySortedListBeacuseImIteratingFromLowToHighThisIsSoFuckingAss[-1]

    

Number_a = 12
Number_b = 24
print(EuclidsAlgorithm(Divisors_of_a_number(Number_a),Divisors_of_a_number(Number_b)))
#oh shit realised i was meant to do this recursively
#CANT BE ASKED I MADE IT THIS IS 