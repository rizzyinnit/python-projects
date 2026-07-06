ask = input("Rock, Paper, or Scissors? ").lower()
if ask not in ["rock", "paper", "scissors"]:
    print("Invalid input. Please choose Rock, Paper, or Scissors.")

elif ask == "rock":
    print("You chose Rock. I choose Paper. I win!")
elif ask == "paper":
    print("You chose Paper. I choose Scissors. I win!")
elif ask == "scissors":
    print("You chose Scissors. I choose Rock. I win!")  

else:
    print("Invalid input. Please choose Rock, Paper, or Scissors.")
    


