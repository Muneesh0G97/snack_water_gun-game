import random

def check(comp,user):
    if(comp==user):
        return 0
    if(comp==0 and user==1):
        return -1
    if(comp==1 and user==2):
        return -1
    if(comp==2 and user==0):
        return -1
    return 1
user=int(input("0 for snake,1 for water, 2 for Gun :"))
comp= random.randint(0,2)
print("You:",user)
print("computer:",comp)
score = check(comp,user)
if score ==0:
    print("It's Draw")
if score==-1:
    print("You loose")
else:
    print("you win!")

