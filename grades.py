import random

def grade():
    for i in range (0,10): 
        score = random.randint(60,101)   
        if score >= 60 and score<70:
            print "Score: ",score,"Your Grade is D"
        elif score >=70 and score<80 :
            print "Score: ",score,"Your Grade is C"
        elif score >=80 and score<90:
            print "Score: ",score,"Your Grade is B"
        elif score >=90 and score<=100 :
            print "Score: ",score,"Your Grade is A"
grade()
