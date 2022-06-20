#problem 1

#Assume s is a string of lower case characters.
#Write a program that counts up the number of vowels 
#contained in the string s. Valid vowels are: 'a', 'e', 'i', 'o', and 'u'. 
#For example, if s = 'azcbobobegghakl', 
#your program should print:
#   Number of vowels: 5

answer = 0
inp = input("type in a string: ")
for char in inp:
    if (char == "a" or char == "i" or char == "o" or char == "u"):
        answer += 1

print("Number of vowels is" , answer)