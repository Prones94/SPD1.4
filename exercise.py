# Problem 1
'''
list1 = [1,2,3,4,5,5,6,7,8,9,]
return True

list2 = [9,4,2,3,4,8,10,11]
return True

list3 = [2,3,4,5,6,7,8,9,0]
return false

Pseudo:
Function of find duplicates( takes in array)
	empty array start
	for number in the array:
		if the number id in the array:
			return True
		else:
			append number to empty array
	return False
'''

#Actual: Simplest yet not most efficient
def find_dup(array):
    dup_array = []
    for number in array:
        if number in array:
            return True
        else:
            dup_array.append(number)
    #Returning false if no dup is found
    return False



# Other Way: Problem 1
'''
Pseudo:
function(array):
	empty dictionary
	for loop over the array
'''
#Code
def find_dup(array):
	dup_dict = {}
	for number in array:
		if dup_dict 
    #Returning false if no dup is found
	return False

# Problem 4
'''
Restate the problem:
Given a string of text and the number k, find the number of words that appear multiple 
times in the tex, up to the number k in the number of words. Return them in an array of 
decreasing order.
ex. I have, I will, I want. It is that I will have the item. I want it. 
k = 3
answer = ["I","have","will"]

Pseudocode:
	- Essentially make a dictogram function that takes in a string
	- Converts to a list, strip spaces and punctuation
	- Go through list and add to dictionary
		- Check if in dictionary
			- Add one to the count value of the dictioanry
		- If not
			- Add to dictionary with count 1
Organize the dictionary by value amounts - hopefully in descending order
Add the key values to a list via k
return list
'''

# Code

def frequent_words(string):
	word_dict = {}
	some_list = []
	return_list = []
	words_list = [line.strip() for line in string]
	if words_list is not None:
		for word in words_list:
			if word not in word_dict:
				word_dict[word] = 1
			else:
				word_dict[word] += 1
			sorted_dict = sorted(word_dict.items(), key = lambda item: item[1], reverse = True)

			for object in sorted_dict:
				some_list.append(object)
			for i range(0..k):
				return_list.append(some_list[i])

	return return_list

# Problem 2
'''
Rephrase Question: Find the halfway point of a list, or the two items in the middle if there isn't a halfway point

Pseudocode:
	- Create Node Class
	
'''