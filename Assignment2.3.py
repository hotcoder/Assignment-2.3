'''
Python program to reverse a word after accepting the input from the user.
'''

word = input("Enter any word : " )

reversedWord=""

for i in reversed(word):
    reversedWord = reversedWord + i

print("Reversed Word : " , reversedWord)