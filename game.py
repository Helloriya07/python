"""
WORKFLOW OF PROJECT:
1-Input fromuser(Rock,paper,scissor)
2-Computer choice(computer will choose randomly not conditionally)
3-Result print

Cases:
A=Rock:
Rock-Rock=tie
Rock-paper=Paper win
Rock-scissor=Rock win

B=Paper:
Paper-Paper=tie
paper-rock=Paper win
paper-scissor=Scissor win

C=Scissor:
Scissor-Scissor=tie
Scissor-rock=rock win
Scissor-paper=Scissor win
"""
import random
#Inputs--
item_list=["Rock","Paper","Scissor"]
user_choice=input("enter what you want to choose")
comp_choice=random.choice(item_list)

print(f"User Choice={user_choice}\n Computer choice={comp_choice}")

#Cases--
if(user_choice==comp_choice):
    print("both chooses same => Match tie")
elif(user_choice=="Rock"):
    if(comp_choice=="Paper"):
     print("Paper covers rock => Computer win")
    else:
      print("Rock smashes scissor => You win")
      
elif(user_choice=="Paper"):
    if(comp_choice=="Scissor"):
     print("Scissor cuts paper=> Computer win")
    else:
      print("Paper covers Rock => You win")

elif(user_choice=="Scissor"):
    if(comp_choice=="Paper"):
     print("Scissor cuts paper=> You win")
    else:
      print("Rock smashes scissor => Computer win")     
