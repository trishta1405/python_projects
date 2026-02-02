from colorama import Fore, Back, Style
import time

print(Fore.CYAN + Style.BRIGHT)
print("🎮 TIC TAC TOE GAME 🎮")
print(Style.RESET_ALL)

print(Fore.BLUE + Style.BRIGHT)
name=input("enter your name:")
print(f"welcome {name}")
time.sleep(1)
print(Style.RESET_ALL)

print(Fore.YELLOW + " _ | _ | _ ")
print(" _ | _ | _ ")
print(" _ | _ | _ ")

time.sleep(1)
print(" ")
print("enter the following number to enter your input on that respective position")

time.sleep(3)
print("1 2 3")
print("4 5 6")
print("7 8 9")
print(Style.RESET_ALL)

list1=['_','_','_','_','_','_','_','_','_']
turn=1

import random

while turn<10:
    print(Fore.MAGENTA + f"\n🔁 Turn {turn}" + Style.RESET_ALL)

    if turn%2==0:
        print(Fore.YELLOW)
        pos=int(input(f"{name} enter ur turn:"))
        if list1[pos-1]=='_':
            list1[pos-1]= "❌"

        else:
            print(Fore.YELLOW)
            print("position is already occupied")
            turn=turn-1

    else:
        print(Fore.YELLOW)
        print("computer's turn")

        time.sleep(2)
        pos=random.randint(1, 9)
        if list1[pos - 1] == '_':
              list1[pos - 1] = "⭕"

        else:
            time.sleep(2)
            print(Fore.YELLOW)
            print("position is already occupied")
            turn=turn-1

    print(Fore.CYAN + Style.BRIGHT)
    print("After turn",turn)
    print("\n", list1[0], "|", list1[1], "|", list1[2])
    print("———+———+———")
    print(" ", list1[3], "|", list1[4], "|", list1[5])
    print("———+———+———")
    print(" ", list1[6], "|", list1[7], "|", list1[8])
    """
    print(list1[0],list1[1],list1[2])
    print(list1[3],list1[4],list1[5])
    print(list1[6],list1[7],list1[8])
    """
    turn+=1
    print(Style.RESET_ALL)

    if (list1[0]=="❌" and list1[1]=="❌" and list1[2]=="❌" or
            list1[0]=="❌" and list1[4]=="❌" and list1[8]=="❌" or list1[0]=="❌" and list1[3]=="❌" and list1[6]=="❌"
        or list1[1]=="❌" and list1[4]=="❌" and list1[7]=="❌" or list1[2]=="❌" and list1[5]=="❌" and list1[8]=="❌"
            or list1[2]=="❌" and list1[4]=="❌" and list1[6]=="❌"
        or list1[3]=="❌" and list1[4]=="❌" and list1[5]=="❌" or list1[6]=="❌" and list1[7]=="❌" and list1[8]=="❌"):
        turn=22
        print(Fore.RED + Style.BRIGHT + f"🏆 congratulation {name} you won! 🏆" + Style.RESET_ALL)

    elif (list1[0]=="⭕" and list1[1]=="⭕" and list1[2]=="⭕" or list1[0]=="⭕" and list1[4]=="⭕" and list1[8]=="⭕"\
            or list1[0]=="⭕" and list1[3]=="⭕" and list1[6]=="⭕" or list1[1]=="⭕" and list1[4]=="⭕" and list1[7]=="⭕"\
          or list1[2]=="⭕" and list1[5]=="⭕" and list1[8]=="⭕"\
            or list1[2]=="⭕" and list1[4]=="⭕" and list1[6]=="⭕" or list1[3]=="⭕" and list1[4]=="⭕" and list1[5]=="⭕"
          or list1[6]=="⭕" and list1[7]=="⭕" and list1[8]=="⭕"):
            turn = 22
            print(Fore.GREEN + Style.BRIGHT + "\n🤖 Computer Wins! 🤖" + Style.RESET_ALL)


if turn!=22:
    print(Fore.CYAN + Style.BRIGHT + "\n🤝 It's a Tie!" + Style.RESET_ALL)