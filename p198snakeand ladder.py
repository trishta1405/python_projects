import random
import time

pos1=0
pos2=0
chance=0
board=[
0,0,0,0,0,0,0,0,0,0,0,
0,0,0,0,0,0,0,0,0,0,
0,0,0,0,0,0,0,0,0,0,
0,0,0,0,0,0,0,0,0,0,
0,0,0,0,0,0,0,0,0,0,
0,0,0,0,0,0,0,0,0,0,
0,0,0,0,0,0,0,0,0,0,
0,0,0,0,0,0,0,0,0,0,
0,0,0,0,0,0,0,0,0,0,
0,0,0,0,0,0,0,0,0,0]

board[3]=57
board[10]=30
board[15]=25
board[33]=52
board[62]=99
board[71]=91

board[57]=2
board[27]=8
board[74]=53
board[86]=75
board[97]=42

print("Welcome to Snake and Ladder Game")
print("2 player game")
print("Reach 100 to win")
name1=input("Enter the name of player1: ")
name2=input("Enter the name of player2: ")
print(" ")
print("")

time.sleep(1)
print("board:")
print("100  99  98  97  96  95  94  93  92  91")
print("81   82  83  84  85  86  87  88  89  90")
print("80   79  78  77  76  75  74  73  72  71")
print("61   62  63  64  65  66  67  68  69  70")
print("60   59  58  57  56  55  54  53  52  51")
print("41   42  43  44  45  46  47  48  49  50")
print("40   39  38  37  36  35  34  33  32  31")
print("21   22  23  24  25  26  27  28  29  30")
print("20   19  18  17  16  15  14  13  12  11")
print("1    2   3   4   5   6   7   8   9   10")
print(" ")
print(" ")

time.sleep(1)
print("ladder= 3 to 56")
print("ladder= 10 to 30")
print("ladder= 15 to 20")
print("ladder= 33 to 52")
print("ladder= 62 to 99")
print("ladder= 71 to 91")
print(" ")
print(" ")

time.sleep(1)
print("snake= 57 to 2")
print("snake= 27 to 8")
print("snake= 74 to 53")
print("snake= 86 to 75")
print("snake= 97 to 42")

time.sleep(1)

while pos1<101 and pos2<101:
        turn=input(f"{name1} press enter to roll the dice ")
        dice=random.randint(1, 6)
        print("dice:", dice)
        pos1=pos1+dice

        if pos1>100:
            pos1=pos1-dice

        if board[pos1]!=0:
            pos1=board[pos1]

        print(f"{name1} position:", pos1)
        print("________________________________________________")

        if pos1 == 100:
            print(f"{name1} wins the game 🎉")
            break

        print(" ")
        turn=input(f"{name2} press enter to roll the dice ")
        dice = random.randint(1, 6)
        print("dice:", dice)
        pos2=pos2+dice

        if pos2>100:
            pos2=pos2-dice

        if board[pos2]!=0:
            pos2=board[pos2]

        print(f"{name2} position:",pos2)
        print("________________________________________________")
        if pos2 == 100:
            print(f"{name2} wins the game 🎉")
            break

        print(" ")

