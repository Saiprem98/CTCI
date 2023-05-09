# Interview Questions for Chatpter 1 Arrays and Strings 

# Is Unique: Implement an algorithm to determine if a string has all unique characters. What if you
# cannot use additional data structures? 
def isUnique(uniqueString):
	if(len(uniqueString)>128):
		return false

	storeChar = [0] * 128
	for i in uniqueString:
		if storeChar[ord(i)] == 1:
			return False
		else:
			storeChar[ord(i)] = 1
	return True

# Check Permutation: Given two strings, write a method to decide if one is a permutation of the
# other. 
# ok two ways we can do this

#First way is to check the length and if the same then sort the strings these sorted strings should be equal to each other 

def checkPerm(a,b):
	if (len(a) != len(b)):
		return False
	sortA = sorted(a)
	sortB = sorted(b)
	if sortA == sortB:
		return True
	else:
		return False

# URLify: Write a method to replace all spaces in a string with '%20'. You may assume that the string
# has sufficient space at the end to hold the additional characters, and that you are given the "true"
# length of the string. (Note: if implementing in Java, please use a character array so that you can
# perform this operation in place.)
# EXAMPLE
# Input: "Mr John Smith ", 13
# Output: "Mr%20John%20Smith" 

def urlify(a):
	return a.replace(" ","%20")


# Palindrome Permutation: Given a string, write a function to check if it is a permutation of
# a palindrome. A palindrome is a word or phrase that is the same forwards and backwards. A
# permutation is a rearrangement of letters. The palindrome does not need to be limited to just
# dictionary words.
# EXAMPLE
# Input: Tact Coa
# Output: True (permutations: "taco cat'; "atco eta·; etc.) 
def palindromePermutation(a):
	count = {}
	oneOdd = False
	for i in range(len(a)):
		count[a[i]] = count.get(a[i],0) + 1
	
	print(count)
	for value in count.values():
		if value%2 == 1:
			if oneOdd:
				return False
			oneOdd = True
	return True 

# One Away: There are three types of edits that can be performed on strings: insert a character,
# remove a character, or replace a character. Given two strings, write a function to check if they are
# one edit (or zero edits) away.
# EXAMPLE
# pale, ple -> true
# pales, pale -> true
# pale, bale -> true
# pale, bae -> false
def oneAway(a,b):
	# determine if we need to check for insert, replace, or remove 
	if(len(a) == len(b)):
		return checkReplace(a,b)
	if(len(a) + 1 == len(b)):
		return checkInsert(a,b)
	if(len(a) - 1  == len(b)):
		return checkInsert(b,a)
	return False 

def checkReplace(a,b):
	oneDiff = False 
	for i in range(len(a)):
		if(a[i] != b[i]):
			if(oneDiff):
				return False
			oneDiff = True 
	return True 

def checkInsert(s1,s2):
	index1 = 0
	index2 = 0

	while(index1 < len(s1) and index2 < len(s2)):
		if(s1[index1] != s2[index2]):
			if(index1 != index2):
				print(index1,index2)
				return False
			index2 += 1
		else:
			index1 +=1
			index2 +=1

	return True


def Stro


def main():
    # print("Hello World!")
    # print(isUnique("Helo"))
    # print(checkPerm("Hello","Hell1o"))
    # print(urlify("Hello World"))
    # print(palindromePermutation("HHeello"))
    # print(oneAway("pale","ple"))

if __name__ == "__main__":
    main()


