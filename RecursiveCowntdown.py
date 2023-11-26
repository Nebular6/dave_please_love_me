import time
def countdown(number):
    if number <= 0:
        return number
    else:
        print(number)
        time.sleep(1)
        countdown(number-1)


countdown(10)