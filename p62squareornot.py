"""
 Take the values of length and breadth of a rectangle from the user and
check if it is a square or not.
"""

length = int(input("please enter the length of the rectangle: "))
breadth = int(input("please enter the breadth of the rectangle: "))

if breadth < length:
    print("it is a rectangle")
elif breadth == length:
    print("it is a square")
else:
    print("it is a rectangle")