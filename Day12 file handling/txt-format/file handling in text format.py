#1. count occurance of word India  in india.txt file

file = open("india.txt", "r")

content = file.read()
content = content.lower()
count = content.count('india')

print(f"The word India occurs {count} time in india.txt")


#2. program to count and display the line starting with "T" in a text file 

file = open("story.txt","r")
count = 0

for line in file:
    if line.startswith("T"):
        print(line.strip())
        count += 1

file.close()
print()
print(f"Total lines starting with 'T': {count}")



# 3. count total numbers of  vowels and consonants in myfile.txt 

file = open("myfile.txt","r")
content = file.read()
file.close()  

content = content.lower()

count = 0  
const = 0  

vowels = ["a", "e", "i", "o", "u"]

for letter in content:
    if letter.isalpha(): 
        if letter in vowels:
            count += 1
        else:
            const += 1

print(f"Total vowels are: {count} Total consonants are: {const}")



# 4.count and display no. of words starting with 'i' in word.txt file
file = open("word.txt","r")
content = file.read()
content = content.lower()
content = content.split()
count =0
words = []
for word in content:
    if word.startwith('i'):
        count+=1
        words.append(word)
print("count of words starting with i",count,words)


#WAP to display the lines having more than five words 

file = open("notes.txt", "r")
for line in file:
    words = line.split()
    if len(words) > 5:
        print(line.strip())
file.close()




