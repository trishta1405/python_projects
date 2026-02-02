"""
Write a program to display all the numbers between m and n input from the keyboard (where m<n, m>0, n>0), check and print
 the numbers that are perfect square. e.g. 25, 36, 49, are said to be perfect square numbers. Use this ,Math.sqrt() , int
"""
import math

num1=int(input("enter number 1:"))
num2=int(input("enter number 2:"))

for i in range(num1,num2+1):
    sqrt=math.sqrt(i)
    if sqrt==int(sqrt):
        print(i,end=" ")



