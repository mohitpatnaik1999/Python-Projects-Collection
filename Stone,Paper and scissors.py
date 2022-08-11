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

lists=[rock,paper,scissors]
user_input=int(input("What do you choose? Type 0 for rock,1 for paper or 2 for scissors.\n"))
print(lists[user_input])
length=len(lists)
computer_input=random.randint(0,length-1)
print("Computer choose:")
print(lists[computer_input])
if lists[user_input]==rock:
  if lists[computer_input]==paper:
    print("You lose")
  elif lists[computer_input]==scissors:
    print("You win")
  else:
    print("Game is drawn")
elif lists[user_input]==paper:
  if lists[computer_input]==rock:
    print("You win")
  elif lists[computer_input]==scissors:
    print("You lose")
  else:
    print("Game is drawn")
elif lists[user_input]==scissors:
  if lists[computer_input]==rock:
    print("You lose")
  elif lists[computer_input]==paper:
    print("You win")
  else:
    print("Game is drawn")
