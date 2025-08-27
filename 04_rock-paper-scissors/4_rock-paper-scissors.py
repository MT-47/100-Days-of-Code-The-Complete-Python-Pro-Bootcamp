import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇

game = [rock, paper, scissors]

Player = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))
if Player != 0 and Player != 1 and Player != 2: 
    print("You typed an invalid number, you lose!") 
else:
  print(game[Player])

  Com = random.randint(0 , 2)
  print("Computer chose:")
  print(game[Com])

  if Player == Com:
      print("It's a draw")
  elif (Com == 0 and Player == 1) or (Com == 1 and Player == 2) or (Com == 2 and Player == 0):
      print("You win!")
  else:
      print("You lose")
