import random
import time

print("\nWelcome to the game!")
print("In this game you will be playing Powerball.")
time.sleep(1)
print("Rules: The game is simple. Choose your first 5 numbers from 1 to 69 and a Powerball number from 1 to 26.")
time.sleep(5)

#your ticket
t1 = int(input("\nPlease choose your first number: "))
t2 = int(input("Please choose your second number: "))
t3 = int(input("Please choose your third number: "))
t4 = int(input("Please choose your fourth number: "))
t5 = int(input("Please choose your fifth number: "))
powerball = input("Please pick a Powerball number from 1 to 26: ")
time.sleep(1)
print(f"\nYour ticket: {t1} {t2} {t3} {t4} {t5} [{powerball}]")
    
#the jackpot
a = random.randint(1,69)
b = random.randint(1,69)
c = random.randint(1,69)
d = random.randint(1,69)
e = random.randint(1,69)
p = random.randint(1,26)
time.sleep(3)
print(f"\nThe jackpot: {a} {b} {c} {d} {e} [{p}]")

#the prizes
