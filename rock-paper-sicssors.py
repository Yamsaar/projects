import random
print("welcome for rock, paper and scissors, playing againts the computer! \n")
 
scissors = '''

   ________
 __'     ___)___
         _______)
      ___________)
       (_____)
 ---,__(_____)
 '''
rock = '''
    _______
---'   _____)
       (_____)
       (_____)
       (_____)
 ---,__(____)
 '''
paper = '''
    _______
---'   _____)___
       (________)
       (________)
       (_______)
 ---,__(______)
 '''

game_images = [rock, paper, scissors]

user_choice = int(input("Please enter you're choice : Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))


if user_choice >= 3 or user_choice < 0:
    print("Invalid number, you lose!")
else:
    print(game_images[user_choice])
    computer_choice = random.randint(0, 2)

    print("computer chose:")

    print(game_images[computer_choice])
      
    if user_choice == 0 and computer_choice == 2:
        print("you win!!")
    elif user_choice == 2 and computer_choice == 0:
        print("you lose!!")
    elif computer_choice > user_choice:
        print("you lose")
    elif computer_choice < user_choice:
        print("you win!!")
    elif computer_choice == user_choice:
        print("It's a draw!")
     
    
