import random
print("Welcome to stone paper scissors game")
user = 0
computer = 0
l = ['stone','paper','scissors']
rounds = int(input("How many rounds you want to play: "))
num = 0
while num<rounds:
    user_choice = input("enter stone paper scissors: ")
    r = random.choice(l)
    if user_choice==r:
        print("no one can won")
    elif user_choice=="stone" and r=="scissors":
        print("user won")
        user+=1
    elif user_choice=="stone" and r=="paper":
        print("computer won")
        computer+=1
    elif user_choice=="paper" and r=="stone":
        print("user won")
        user+=1
    elif user_choice=="paper" and r=="scissors":
        print("computer won")
        computer+=1  
    elif user_choice=="scissors" and r=="paper":
        print("user won")
        user+=1
    elif user_choice=="scissors" and r=="stone":
        print("computer won")
        computer+=1      
        
    num +=1
print(f"user win {user} rounds")   
print(f"computer win {computer} rounds")    