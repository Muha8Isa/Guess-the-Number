import random
from replit import clear

def welcome():
  logo = (''' d888b  db    db d88888b .d8888. .d8888.      d888888b db   db d88888b      d8b   db db    db .88b  d88. d8888b. d88888b d8888b.      db 
  88' Y8b 88    88 88'     88'  YP 88'  YP      `~~88~~' 88   88 88'          888o  88 88    88 88'YbdP`88 88  `8D 88'     88  `8D      88 
  88      88    88 88ooooo `8bo.   `8bo.           88    88ooo88 88ooooo      88V8o 88 88    88 88  88  88 88oooY' 88ooooo 88oobY'      YP 
  88  ooo 88    88 88~~~~~   `Y8b.   `Y8b.         88    88~~~88 88~~~~~      88 V8o88 88    88 88  88  88 88~~~b. 88~~~~~ 88`8b           
  88. ~8~ 88b  d88 88.     db   8D db   8D         88    88   88 88.          88  V888 88b  d88 88  88  88 88   8D 88.     88 `88.      db 
   Y888P  ~Y8888P' Y88888P `8888Y' `8888Y'         YP    YP   YP Y88888P      VP   V8P ~Y8888P' YP  YP  YP Y8888P' Y88888P 88   YD      YP''')
  
  print(logo)
  print('''\nWelcome to the Number Guessing Game!
  I'm thinking of a number between 1 and 100.''')

welcome()

generate = random.randint(1,100)

def play():
  
  def lives(life):
    return life
    
  while True:
    choose = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    if choose == "easy":
      life = 10
      print("You chose easy so you have 10 attempts")
      break
    elif choose == "hard":
      life = 5
      print("You chose hard so you have 5 attempts")
      break
    else:
      print("\033[31mInvalid data! Please type either 'easy' or 'hard'\033[0m")
      
  def guess(life): 
    while life != 0:
      guess = int(input("Guess the number: "))
      if guess < (generate - 5):
        print("Too low")
      elif guess > (generate + 5):
        print("Too high")
      elif guess < generate:
        print("Low but you are close")
      elif guess > generate:
        print("High but you are close")
      elif guess == generate:
        print(f"Congrats, you guessed the number {generate}")
        break
        
      life -= 1
      if life > 0:
        print(f"You have {life} lives remaining.")
      else:
        print("You lose")
  guess(life)

play()

while True:
  play_again = input("Do you want to play again? type 'yes' or 'no': ").lower()
  if play_again == "yes":
    clear()
    welcome()
    play()
  elif play_again ==  "no":
    print("Good bye :)")
    break
  else:
      print("\033[31mInvalid data! Please type either 'yes' or 'no'\033[0m")
  
