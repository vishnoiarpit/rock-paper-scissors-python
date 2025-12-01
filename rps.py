# -1 is for rock,
# 0 is for paper
# 1 for scissor
import random
def game():
    #computer=random.randint(-1,1)
    computer=random.choice([-1,0,1])
    user=(input("Choose b/w Rock , Paper & Scissor ")).lower()
    map_dict={
                -1:"rock",
                 0:"paper",
                 1:"scissor"
            }
    com=map_dict.get(computer)
    print(f"Computer Choice: {com}")
    print(f"Your Choice: {user}")
    if user not in map_dict.values():
          print("Invalid Input")
          return
    if(com == user):
       print("It is a Draw!")
    else:
          if(com == "rock" and user=="scissor"):
                 print("You Lose!")
          elif(com == "rock" and user=="paper"):
                 print("You Win!")
          elif(com == "paper" and user=="rock"):
                 print("You Lose!")
          elif(com == "paper" and user=="scissor"):
                 print("You Win!")
          elif(com == "scissor" and user=="paper"):
                 print("You Lose!")
          elif(com == "scissor" and user=="rock"):
                 print("You Win!")
        #   else:
        #          print("Invalid Input")
                 

while(True):
      playagain=input("Do want to play again?Yes/No ").lower()
      if(playagain == "yes"):
            game()
      elif(playagain == "no"):
            print("Good Bye")
            break
      else:
            print("Invalid Input,Do you want to Play Again(Yes/No)")
            

