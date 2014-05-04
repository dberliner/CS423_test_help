import sys
import math

positions = []
current = int(raw_input("Enter starting point: "))
dir = int(raw_input("Enter starting direction (0=decreasing, 1=increasing): "))

while True:    #Gather the input
	n = raw_input("Input integer position (inter nothing to end input): ")
	if n == "":
		break  
	n=int(n)
	positions.append(n)

#Start by printing the starting point
print(str(current) + ", ")

# Go though the entire list and print the shortest path
# This is n^2 but of a small list
while len(positions) > 0:
	diff=sys.maxint
	index=0
	i=0
	for pos in positions:
		if diff > (math.fabs(pos-current)):
			if (current < pos and dir == 1) or (current > pos and dir == 0):
				diff=math.fabs(pos-current)
				index=i
		i=i+1
	if diff==sys.maxint:
		if dir == 0:
			current=sys.maxint
		else:
			current=0
	else:
		current=positions.pop(index)
		print(str(current) + ", ")
raw_input("Press enter to continue")