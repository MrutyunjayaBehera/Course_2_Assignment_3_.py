import math
import os
import random
import re
import sys


"""n = input("enter the  number: ")
n = int(n)

if n % 2 != 0:
	print("Weird")
else:
	if n > 2 and n < 5:
		print("Not Weird")
	elif n > 6 and n < 20:
		print("Weird")
	elif n > 20:
		print("Not Weird")"""

"""n = input("enter the number: ")
n = int(n)
for i in range(1,n+1):
    print(i, end = "")"""

"""x = input("raw_input1: ")
x = int(x)
y = input("raw_input2: ")
y = int(y) 
z = input("raw_input3: ")
z = int(z)
n = input("raw_input4: ")
n = int(n)

print([[a,b,c] for a in range(0,x+1) for b in range(0,y+1) for c in range(0,z+1) if a + b + c != n])"""

"""k = input()
arr = []
arr = k.split(" ")
print(arr)

large = max(arr)
n = len(arr)
for i in range(n):
	if large == max(arr):
		arr.remove(max(arr))
print(max(arr))"""

"""if __name__ == '__main__':
    
    score_list = []
    mark_sheet = []

for _ in range(int(input())):
    name = input()
    score = float(input())
    mark_sheet.append([name,score])
    score_list.append(score)

second_lowest_mark = sorted(list(dict.fromkeys(score_list)))[1]

for name,marks in sorted(mark_sheet):
    if marks == second_lowest_mark:
        print(name)"""

"""my_str = input()
print(my_str.isalnum())
print(my_str.isalpha())
print(my_str.isdigit())
print(my_str.islower())
print(my_str.isupper())"""

#maps and filter

"""nums = [11, 22, 33, 44, 55]
result = list(map(lambda x: x+5, nums))
print(result)"""

"""def countdown():
	i = int(input("enter the value of i: "))
	while i > 0:
		yield i
		i -= 1

for i in countdown():
	print(i)"""


#QUESTION 1 --> The dictionary Junior shows a schedule for a junior year semester. The key is the course name and the 
#value is the number of credits. Find the total number of credits taken this semester and assign it to the variable credits. 
#Do not hardcode this – use dictionary accumulation!

Junior = {'SI 206':4, 'SI 310':4, 'BL 300':3, 'TO 313':3, 'BCOM 350':1, 'MO 300':3}

credits = 0
credits = 0
for jn in Junior.keys():
	credits = credits + Junior[jn]

print(credits)


#QUESTION 2--> Create a dictionary, freq, that displays each character in string str1 as the key and its frequency 
#as the value.

str1 = "peter piper picked a peck of pickled peppers"
freq = {}

for x in str1:
    if x not in freq:
        freq[x] = 0
    freq[x] = freq[x] + 1
print(freq)


#QUESTION 3-->Provided is a string saved to the variable name s1. Create a dictionary named counts that contains each
#letter in s1 and the number of times it occurs.

s1 = "hello"

counts = {}
for x in s1:
    if x not in counts:
        counts[x] = 0
    counts[x] = counts[x] + 1
print(counts)


#QUESTION 4-->Create a dictionary, freq_words, that contains each word in string str1 as the key and its frequency
#as the value.

str1 = "I wish I wish with all my heart to fly with dragons in a land apart"
real = []
real = str1.split(" ")

freq_words = {}
for x in real:
    if x not in freq_words:
        freq_words[x] = 0
    freq_words[x] = freq_words[x] + 1
    
print(freq_words)


#QUESTION 5-->Create a dictionary called wrd_d from the string sent, so that the key is a word and the value is how many
#times you have seen that word.

sent = "Singing in the rain and playing in the rain are two entirely different situations but both can be good"
real = []
real = sent.split(" ")

wrd_d = {}
for x in real:
    if x not in wrd_d:
        wrd_d[x] = 0
    wrd_d[x] = wrd_d[x] + 1
print(wrd_d)


#QUESTION 6-->Create the dictionary characters that shows each character from the string sally and its frequency. 
#Then, find the most frequent letter based on the dictionary. Assign this letter to the variable best_char.

sally = "sally sells sea shells by the sea shore"
characters = {}
for x in sally:
    if x not in characters:
        characters[x] = 0
    characters[x] = characters[x] + 1
ks = list(characters.keys())
best_char = ks[0]
for y in ks:
    if characters[y]>characters[best_char]:
        best_char = y
        
print("the most frequent chracter is", best_char)


#QUESTION 7-->Find the least frequent letter. Create the dictionary characters that shows each character from string 
#sally and its frequency. Then, find the least frequent letter in the string and assign the letter to the variable 
#worst_char.

sally = "sally sells sea shells by the sea shore and by the road"

characters = {}
for x in sally:
    if x not in characters:
        characters[x] = 0
    characters[x] = characters[x] + 1
ks = list(characters.keys())
worst_char = ks[0]
for y in ks:
    if characters[y]<characters[worst_char]:
        worst_char = y
        
print("the least frequent chracter is", worst_char)


#QUESTION 8-->Create a dictionary named letter_counts that contains each letter and the number of times it occurs in 
#string1. Challenge: Letters should not be counted separately as upper-case and lower-case. Intead, all of them should be
#counted as lower-case.

string1 = "There is a tide in the affairs of men, Which taken at the flood, leads on to fortune. Omitted, all the voyage of their life is bound in shallows and in miseries. On such a full sea are we now afloat. And we must take the current when it serves, or lose our ventures."

string1 = string1.lower()
letter_counts = {}
for x in string1:
    if x not in letter_counts:
        letter_counts[x] = 0
    letter_counts[x] = letter_counts[x] + 1
print(letter_counts)


#QUESTION 9-->Create a dictionary called low_d that keeps track of all the characters in the string p and notes how many 
#times each character was seen. Make sure that there are no repeats of characters as keys, such that “T” and “t” are both 
#seen as a “t” for example.

p = "Summer is a great time to go outside. You have to be careful of the sun though because of the heat."

p = p.lower()
low_d = {}
for x in p:
    if x not in low_d:
        low_d[x] = 0
    low_d[x] = low_d[x] + 1
print(low_d)

#ENJOY


