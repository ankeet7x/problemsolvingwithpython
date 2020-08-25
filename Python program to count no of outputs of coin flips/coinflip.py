import random

options = [ 'H', 'T']

tailcount = 0
headcount =0
n = input("Input no. of flips you want")
i = int(n)
while(i > 0):
    flipped = random.choice(options)
    
    if(flipped == 'H'):
        headcount = headcount+1
    else:
        tailcount = tailcount+1
    i = i-1
print("No. of heads : " + str(headcount))
print("No. of tails : " + str(tailcount))
