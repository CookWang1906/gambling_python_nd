import random
import time

def play():
    print("\n1. Play Powerball")
    print("2. Play Mega Millions")
    print("3. Play Lucky for life")
    print("4. Play Cash 5")
    print("5. Play Pick 4")
    print("6. Play Pick 3")
    print("7. Play Carolina Keno")
    print("8. Play Fast Mode")
    print("9. Play Instant Scratch-Off")
    print("0. End Game")
    choice = int(input("Please choose a game to play: "))
    
    if choice == 1:
        powerball()
    elif choice == 2:
        megamillions()
    elif choice == 3:
        luckyforlife()
    elif choice == 4:
        cash5()
    elif choice == 5:
        pick4()
    elif choice == 6:
        pick3()
    elif choice == 7:
        carolinakeno()
    elif choice == 8:
        fastmode()
    elif choice == 9:
        instantoff()
    elif choice == 0:
        print()
    else:
        print("If you see this, you are a bitch")
        return play()
    
def powerball():
    print("Welcome to Powerball! One of the most exciting games in the known universe.")
    time.sleep(1)
    print("Rules: Choose your first 5 numbers from 1 to 69 and a Powerball number from 1 to 26.")
    time.sleep(5)
    
    
    
    
    
    
def megamillions():
    print("Game")







def luckyforlife():
    print("Game")








def cash5():
    print("Game")
    
    
    
    
    
    
    
    
def pick4():
    print("Game")
    
    
    
    
    
    
    
    
def pick3():
    print("Game")
    
    
    
    
    
    
    
    
def carolinakeno():
    print("Game")
    
    
    
    
    
    
    
def fastmode():
    print("Game")
    
    
    
    
    
    
    
def instantoff():
    print("Game")
    
 
 
 
 
 
 
 
play()