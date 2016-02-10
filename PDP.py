# This code will run in python 3.4.3 on OS X Yosemite Version 10.10.5
# test distances = {2 2 3 3 4 5 6 7 8 10}


# ---------------------------------------------------------------------------------

# Print the introductory statement
print ("This is an implementation of the Partial Digest Problem by Aly Listhaus")

# ---------------------------------------------------------------------------------

# First, we need to ask the user how many points they want to have
# Can specify a condition i.e. "Pick the number of points (>= 2 and <= 10): "
points = int(input("Pick the number of points: ")) # print the number of points selected

"""
# If we specifed a condition, we would check that the number they gave is okay. If not, ask again.
if (points < 2 or points > 10):
	points = input("That number is not acceptable. Pick the number of points (>= 2 and <= 10): ")
"""


# Use the selected number of points to identify the number of distances using the combinations formula
import math							# import the match package so the factorial function can be used

def nCr(n,r):						# define a function that takes two inputs: n and 5
    f = math.factorial				# perform the math.factorial function and assign it to f
    return f(n) / f(r) / f(n-r)		

distances = nCr(points,2)			# assign the combinations formula output to the variable distances
print ("The number of distances you can input is:", distances) # print the number of distances the user can input


# Next, we need to set up an empty list called distances for the user to put elements into
listofdistances = []

# Then, we ask the user to input distances up to a the max, given their points selection
# Note: to break this loop, enter a non-integer
maxLengthList = distances
while len(listofdistances) < maxLengthList:
    item = int(input("Enter a distance: "))
    listofdistances.append(item)
    print ("Here's your list of distances so far:", listofdistances)
print ("Your final list of distances is:", listofdistances)


# ---------------------------------------------------------------------------------

# Set up the output list where we will store the points' marks on the axis
output = [0] 	# The first point is always set at 0

# Set up the deltax list where will will store the used distances
deltax = []

# First we need to sort the list of distances so that the first element is the biggest number
listofdistances.sort(reverse=True)
print ("Here's the sorted list of distances:", listofdistances)

# From the sorted list, we pull out the biggest number
x = listofdistances[0] 	# Because it's in descending order, the value at index 0 is the biggest
print ("Here's the biggest distance:", x)

# Now we add the biggest distance to the output
output.append(x)				# Add the biggest distance 
output.sort(reverse=False)		# Sort the output in ascending order
print ("Here's your output so far:", output)

# Remove the item we just appended to the output from the original list
listofdistances.remove(x)
deltax.append(x)
listofdistances.sort(reverse=True)
print ("Here's the revised original list of distances:", listofdistances)

# ---------------------------------------------------------------------------------

for i in listofdistances:
	a = 0 + i	# a will be 0 plus the element (i.e. a = 0 + 7 = 7) - coming from the left
	z = x - i	# z will be the biggest number minus the element (i.e. 10 - 7 = 3) - coming from the right
	if a in listofdistances:		# if a is in the list of distances, do the following
		output.append(i)			# put a in the output list
		output.sort(reverse=False)	# sort the output list
		listofdistances.remove(i)	# remove the distance i from the list of distances
		deltax.append(i)			# add i to the list of used distances
		print ("List of distances:", listofdistances)		
		print ("Output:", output)
		print ("Deltax:", deltax)
		for j in output:							# check what other distances we can check off by looping through the output
			if abs(j - i) in listofdistances:		# subtract i from each element in the output and if it's in the list of distances:
				listofdistances.remove(abs(j - i))	# remove this new distance that we found (j - i) from the list of distances
				deltax.append(abs(j - i))			# add j - i to the list of used distances
				print ("List of distances:", listofdistances)		
				print ("Output:", output)
				print ("Deltax:", deltax)
	elif z in listofdistances:		# if a isn't in the list of distances but z is, do the following
		output.append(i)			# put z in the output list
		output.sort(reverse=False)	# sort the output list
		listofdistances.remove(i)	# remove the distance i from the list of distances
		deltax.append(i)			# add i to the list of used distances
		print ("List of distances:", listofdistances)			
		print ("Output:", output)
		print ("Deltax:", deltax)
		for j in output:							# check what other distances we can check off by looping through the output
			if abs(j - i) in listofdistances:		# subtract i from each element in the output and if it's in the list of distances:
				listofdistances.remove(abs(j - i))	# remove this new distance that we found (j - i) from the list of distances
				deltax.append(abs(j - i))			# add i to the list of used distances
				print ("List of distances:", listofdistances)		
				print ("Output:", output)
				print ("Deltax:", deltax)
	else:
		print ("This isn't solvable!")

print ("Deltax:", deltax)
print ("Output:", output)
print ("List of distances:", listofdistances)		# check what our list of distances looks like