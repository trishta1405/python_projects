"""
. You want to replace tiles in your bathroom which is exactly square and 5.5
feet is its length. If tiles cost 500 rs per square feet, how much will be the
total cost to replace all tiles. Calculate and print the cost using python
"""
length=float(input("please enter the length of your bathroom in feet:"))
cost=int(input("please enter the cost of tile per sqr feet:"))
area=length*length
#print("area of bathroom=",area)
print("cost to replace all the tile=",area*cost)
