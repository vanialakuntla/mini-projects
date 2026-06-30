import random

choices = ["rock","paper","scissor"]
user = input("Enter rock paper or scissor:") 

computer = random.choice(choices)

print("you choose:",user)
print("computer choose:",computer)

if user == computer:
    print("It's Tie!!!")

elif(user == "rock" and computer == "scissor") or\
    (user == "paper" and computer == "rock") or\
    (user == "scissor" and computer == "paper"):
    print ("you win!!")
else:
    print("computer wins!!")    