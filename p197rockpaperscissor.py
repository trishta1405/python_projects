from colorama import Fore, Back, Style
import time
import random

print(Fore.CYAN + Style.BRIGHT)
print("🎮 ROCK PAPER SCISSOR 🎮")
print(Style.RESET_ALL)

print(Fore.BLUE + Style.BRIGHT)
name=input("enter your name:")
print(f"welcome {name}")
time.sleep(1)
print(Style.RESET_ALL)

list1 = ["rock", "paper", "scissor"]

print(Fore.YELLOW + "Rules:")
print("Rock ✊ beats Scissor ✌️")
print("Scissor ✌️ beats Paper 🖐️")
print("Paper 🖐️ beats Rock ✊")
print(Style.RESET_ALL)

print(" ")

time.sleep(3)

round=3
turn=1
user=0
comp=0

for i in range(1,round+1):
    print(Fore.MAGENTA + f"\n🔁 Turn {turn}" + Style.RESET_ALL)
    turn=turn+1

    user_choice=input(Fore.BLUE + "Enter rock✊ / paper🖐️ / scissor✌️: " + Style.RESET_ALL)
    while user_choice not in list1:
        user_choice = input(Fore.RED + "Invalid choice! Try again: " + Style.RESET_ALL)

    comp_choice=random.choice(list1)
    print(Fore.BLUE + f"comp_choice: {comp_choice}" + Style.RESET_ALL)

    if user_choice == comp_choice:
            print(Fore.WHITE + "It's a Tie!" + Style.RESET_ALL)

    elif (user_choice=="rock" and comp_choice == "scissor") or \
                (user_choice=="paper" and comp_choice == "rock") or \
                (user_choice=="scissor" and comp_choice == "paper"):
            print(Fore.GREEN + "You won this round!" + Style.RESET_ALL)
            user=user+1

    else:
            print(Fore.RED+"💻 Computer wins this round!" + Style.RESET_ALL)
            comp= comp+1

    time.sleep(1)
tie= user==comp
if user>comp:
        print(Fore.GREEN+"🏆 CONGRATULATIONS! YOU WON THE GAME 🏆")
elif user<comp:
        print(Fore.RED+"COMPUTER WON THE GAME")
elif tie>user or tie:
        print("ITS A TIE!")
else:
    print(Fore.YELLOW+"TIE")
print(Style.RESET_ALL)






