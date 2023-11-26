#triangular numbers
def triangular(n):
    if n <= 1:      #basec
        return 1
    else:           #recursed
        return n + triangular(n-1)


print(triangular(4))          #this works and it fills me with joy