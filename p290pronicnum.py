"""
Write a program to input a number and check and print whether it is a Pronic number or not. [Pronic number is the number which is the product of two consecutive integers.]

Examples:
12 = 3 * 4
20 = 4 * 5
42 = 6 * 7
"""
num = int(input("Enter a number:"))
c=0
for i in range(1, num):
    if i*(i+1)==num:
        c=1
        print(num, "=", i, "*", i + 1)
        break
if c==1:
    print("pronic number")
else:
    print("not a pronic number")


