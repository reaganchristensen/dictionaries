#Write a program that reads the contents of a text file (you can use this file - sometext.txt Download sometext.txt). 
#The program should create a dictionary in which the keys are the individual words found in the file and the values are the number of times each word appears. 
#For example, if the word “the” appears 128 times, the dictionary would contain an element with 'the' as the key and 128 as the value. 
#The program should display the frequency of each word.

txtfile = open('sometext.txt', 'r')

txtfileobject = txtfile.read()

txtfile_clean = txtfileobject.split()

word_frequency = {}

for word in txtfile_clean:
    if word in word_frequency:
        word_frequency[word] += 1
    else:
        word_frequency[word] = 1

for words,value in word_frequency.items():
    print(f"{words}: {value}\n")
