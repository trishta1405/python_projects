from colorama import Fore, Style
import time
import random

# Title
print(Fore.CYAN + Style.BRIGHT)
print("🎮 TIC TAC TOE GAME 🎮")
print(Style.RESET_ALL)

# Initial board display
print(Fore.YELLOW + " _ | _ | _ ")
print(" _ | _ | _ ")
print(" _ | _ | _ ")
print(Style.RESET_ALL)

print("\nEnter the number to choose position:\n")
print(Fore.GREEN + " 1 | 2 | 3 ")
print(" 4 | 5 | 6 ")
print(" 7 | 8 | 9 ")
print(Style.RESET_ALL)

list1 = ['_','_','_','_','_','_','_','_','_']
turn = 1

while turn < 10:
    print(Fore.MAGENTA + f"\n🔁 Turn {turn}" + Style.RESET_ALL)

    if turn % 2 == 0:
        pos = int(input(Fore.BLUE + "Rahul (❌) enter your move: " + Style.RESET_ALL))
        if list1[pos-1] == '_':
            list1[pos-1] = Fore.RED + "❌" + Style.RESET_ALL
        else:
            print(Fore.RED + "❗ Position already occupied" + Style.RESET_ALL)
            turn -= 1

    else:
        print(Fore.YELLOW + "🤖 Computer is thinking..." + Style.RESET_ALL)
        time.sleep(1)
        pos = random.randint(1, 9)
        if list1[pos-1] == '_':
            list1[pos-1] = Fore.GREEN + "⭕" + Style.RESET_ALL
        else:
            turn -= 1

    # Print board
    print("\n", list1[0], "|", list1[1], "|", list1[2])
    print("———+———+———")
    print(" ", list1[3], "|", list1[4], "|", list1[5])
    print("———+———+———")
    print(" ", list1[6], "|", list1[7], "|", list1[8])

    # Win conditions
    if (list1[0]==list1[1]==list1[2]!="_" or
        list1[3]==list1[4]==list1[5]!="_" or
        list1[6]==list1[7]==list1[8]!="_" or
        list1[0]==list1[3]==list1[6]!="_" or
        list1[1]==list1[4]==list1[7]!="_" or
        list1[2]==list1[5]==list1[8]!="_" or
        list1[0]==list1[4]==list1[8]!="_" or
        list1[2]==list1[4]==list1[6]!=""):

        if "❌" in list1:
            print(Fore.RED + Style.BRIGHT + "\n🏆 Rahul Wins! 🏆" + Style.RESET_ALL)
        else:
            print(Fore.GREEN + Style.BRIGHT + "\n🤖 Computer Wins! 🤖" + Style.RESET_ALL)
        turn = 22

    turn += 1

if turn != 22:
    print(Fore.CYAN + Style.BRIGHT + "\n🤝 It's a Tie!" + Style.RESET_ALL)
