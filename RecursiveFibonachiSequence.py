#try to complete this
def fibonacci(n):
    if n == 0:#base case 1
        return 0
    elif n == 1:#base case 2
        return 1
    else:# recursive case
        return fibonacci(n-1) + fibonacci(n-2)

for i in range(int(input(()))): # number inputted will be the nth term of the fibonachi returned
    print(fibonacci(i))         #prints each time, looks nicer hehe