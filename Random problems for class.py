#Joseph Fabisevich
#106098624
#Homework 3

#Problem 1
#Check the lists length's against the last list it just checked.
def isMatrix(listy):
	for i in range(1, len(listy)):
		if(len(listy[i-1]) != len(listy[i])):
			return False
	return True
	
print("1: " + str(isMatrix([[1, 2], [4, 5], [6, 7]])))


#Problem 2
#Take the ith element from each list and build a new list out of it.
def transpose(listy):
	returnlist = []
		
	for i in range(0, len(listy[0])):
		appendMe = []
		for j in range(0, len(listy)):
			appendMe.append(listy[j][i])
		returnlist.append(appendMe)
				
	return returnlist
				
print("2: " + str(transpose([[1, 2, 3, 4], [4, 5, 6, 7], [7, 8, 9, 0]])))


#Problem 3
#Go down the rows and columns. If they are the same, add a 1, otherwise 0.
def identityMatrix (total):	
	   return [[1 if row == column else 0 
			for column in range(0, total)] 
				for row in range(0, total)];

print("3: " + str(identityMatrix(3)));


#Problem 4
#Return a new list using list comprehension with both values added.
def addPolynomails(list1, list2):
	x = []
	y = []
	
	if(len(list1) < len(list2)):
		x = list1
		y = list2
	else:
		x = list2
		y = list1

#Sorry, had to use a for loop... but I didn't use it for the actual adding, just like the specs said.
#Appended extra 0's to make the lengths match up for later adding.
	for i in range(len(x), len(y)):
		x.append(0)

	return [list1[i] + list2[i]
				for i in range(0, len(y))];
					
print("4: " + str(addPolynomails([1, 2, 3], [4, 5, 6, 7])))


#Problem 5
#Take the dict value if the dict key matches the list[i] and swap it in.
def translate(l, d):
	for i in range(0, len(l)):
		if(d.has_key(l[i])):
			l[i] = d.get(l[i])
	return l

print "5: " + str(translate([1,2,3,4], {1:10, 3:15}))


#Problem 6
#It will return true if there is an exact match, otherwise false.
cache = {}

def change(S, D):
	if (S,D) in cache:
   		return cache[S, D]
	if S == 0:
   		ret = True
	elif not D:
   		ret = False
	elif S < 0:
   		ret = False
	else:
   		ret = change(S-D[0], D) or change(S, D[1:])
		
	cache[S, D] = ret

	return ret

print("6: This problem can be solved with these coins: " + str(change(26, (25, 11, 3))))

#Problem 7
#Fill up a dictionary with the proper values, for all others in the range have nothing print out for the number.
def histogram(filename):
	dictionary = dict()
	
	#Could not find integer.max. Need to have the min and max
	#in this scope for later use.
	min = 2147483647;
	max = -2147483647;
	
	#Read the file
	txt = open(filename)
	
	#For each line, check if it is already in the dictionary.
	#If it is, add 1 to the value of the key that it is representing.
	#Else, make a new entry in the dictionary, and say there is 1 of it.
	for line in iter(txt):
		if(dictionary.has_key(int(line))):
			dictionary[int(line)] = dictionary[int(line)]+1
		else:
			dictionary[int(line)] = 1
			if(int(line) >= max):
				max = int(line) + 1
			if(int(line) <= min):
				min = int(line)
				
	txt.close()	
		
	k = dictionary.keys()
	k.sort()
	
	for i in range(min, max):
		if(i in k):
			print "%s: %s" % (i, printStars(int(dictionary[i])))
		else:
			print "%s:" % i

#Helper function for 7
def printStars(stars):
	starsString = ""
	for i in range(0, stars):
		starsString += "*"
	
	return starsString
	
histogram("test.txt")