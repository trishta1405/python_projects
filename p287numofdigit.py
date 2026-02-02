#Write a program to input a number and count the number of digits. The program further
# checks whether the number contains an odd number of digits or even number of digits.

c=0
num=int(input("Enter a number: "))

while num>0:
    c=c+1
    num=num//10
print("number of digits:", c)

if c%2==0:
    print("even number of digits")
else:
    print("odd number of digits")