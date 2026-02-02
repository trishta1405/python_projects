print("_ _ _")
print("_ _ _")
print("_ _ _")
print(" ")
print("1 2 3")
print("4 5 6")
print("7 8 9")

list1=['_','_','_','_','_','_','_','_','_']
turn=1
while turn<10:
    print("After turn", turn)

    if turn%2==0:
        pos=int(input("Rahul enter ur turn "))
        if list1[pos-1]=='_':
            list1[pos-1]= "❌"

        else:
            print("position is already occupied")
            turn=turn-1

    else:
        pos=int(input("nikita enter ur turn "))
        if list1[pos-1]=='_':
            list1[pos - 1] = "⭕"

        else:
            print("position is already occupied")
            turn=turn-1


    print("After turn",turn)
    print(list1[0],list1[1],list1[2])
    print(list1[3],list1[4],list1[5])
    print(list1[6],list1[7],list1[8])

    turn+=1

    if list1[0]=="X" and list1[1]=="X" and list1[2]=="X":
        turn=22
        print("rahul won")
    elif list1[0]=="o" and list1[1]=="o" and list1[2]=="o":
            turn = 22
            print("nikita won")
    elif list1[0]=="X" and list1[4]=="X" and list1[8]=="X":
            turn = 22
            print("rahul won")
    elif list1[0]=="o" and list1[4]=="o" and list1[8]=="o":
            turn=22
            print("nikita won")
    elif list1[0]=="X" and list1[3]=="X" and list1[6]=="X":
            turn=22
            print("rahul won")
    elif list1[0]=="o" and list1[3]=="o" and list1[6]=="o":
            turn=22
            print("nikita won")
    elif list1[1]=="X" and list1[4]=="X" and list1[7]=="X":
            turn=22
            print("rahul won")
    elif list1[1]=="o" and list1[4]=="o" and list1[7]=="o":
            turn=22
            print("nikita won")
    elif list1[1]=="X" and list1[4]=="X" and list1[7]=="X":
            turn=22
            print("rahul won")
    elif list1[1]=="o" and list1[4]=="o" and list1[7]=="o":
            turn=22
            print("nikita won")
    elif list1[2]=="X" and list1[5]=="X" and list1[8]=="X":
            turn=22
            print("rahul won")
    elif list1[2]=="o" and list1[5]=="o" and list1[8]=="o":
            turn=22
            print("nikita won")
    elif list1[2]=="X" and list1[4]=="X" and list1[6]=="X":
            turn=22
            print("rahul won")
    elif list1[2]=="o" and list1[4]=="o" and list1[6]=="o":
            turn=22
            print("nikita won")
    elif list1[3]=="X" and list1[4]=="X" and list1[5]=="X":
            turn=22
            print("rahul won")
    elif list1[3]=="o" and list1[4]=="o" and list1[5]=="o":
            turn=22
            print("nikita won")
    elif list1[6]=="X" and list1[7]=="X" and list1[8]=="X":
            turn=22
            print("rahul won")
    elif list1[6]=="o" and list1[7]=="o" and list1[8]=="o":
            turn=22
            print("nikita won")

if turn!=22:
    print("tie")

