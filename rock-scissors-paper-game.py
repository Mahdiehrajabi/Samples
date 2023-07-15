import random


def game():
  user = input("Enter one of them rock, paper, scissors: ")
  actions = ["rock", "paper", "scissors"]
  computer = random.choice(actions)
  print(f"\nYour choise {user}, computer choise {computer}.\n")

  if user == computer:
    print("the choice of both are same.(tie)")
  elif user == "rock" :
    if computer == "scissors" :
      print("you are winner.")
  elif user == "paper" :
    if computer == "scissors" :
      print("computer is winner.")
  elif user == "rock" :
    if computer =="paper":
     print("computer is winner")
  elif user =="scissors":
    if computer == "paper" :
      print ("you are winner")
  elif user == "paper" :
    if computer =="rock" :
      print ("computer is winner")
  elif user == "scissors" :
    if computer =="rock" :
      print("computer is winner")

  else:
    print("sorry, try again")

game()