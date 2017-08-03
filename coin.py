import random

def coin():
    head=0
    tail=0
    for count in range (1,5001):
        rand = random.randint(0,1)
        # print rand
        if rand == 1:
            head +=1
            print "attempt: ",count,"it is a head", head

        else :
            tail+=1
            print "attemp: ",count, "it is a tail", tail
coin()

