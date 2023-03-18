# program to display unique vowels present in the word/sentence : 

'''

vowels = ['a','e','i','o','u']
word = input('Enter some word/sentence to search vowels : ')
found = []
for letter in word :
	if letter in vowels :
		if letter not in found :
			found.append(letter)
print(found)
print("The no. of different vowels present in '",word,"' is : ",len(found))

'''

'''

vowels = ['a','e','i','o','u','A','E','I','O','U']
word = input('Enter some word/sentence to search vowels : ')
found = []
for letter in word :
	if letter in vowels :
		if letter not in found :
			found.append(letter)
print(found)
print("The no. of different vowels present in '",word,"' is : ",len(found))

'''


vowels = ['a','e','i','o','u']
word = input('Enter some word/sentence to search vowels : ')
found = []
for letter in word :
	if letter.lower() in vowels :
		if letter.lower() not in found :
			found.append(letter.lower())
print(found)
print("The no. of different vowels present in '",word,"' is : ",len(found))
