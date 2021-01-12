import time

# this gives random numbers from 0 to x
def randomNum(x):
    random=int(time.time()*1000)
    random %= x
    return random

print(randomNum(100))
