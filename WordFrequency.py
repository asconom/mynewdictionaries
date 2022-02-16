# open text file
infile = open('AI.txt')

#Create reader
read = infile.read()

# create dictionary
word_count = {}

#remove punctuation
punctuation = '''!()-[]};:{"\,<>./?@#$%^&*_~'''
for letter in read:
    if letter in punctuation:
        read = read.replace(letter, '')

#Split text line by word
words = read.split()

#add word count to dictionary
for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1


for key in word_count:
    print(key + ': ' + str(word_count[key]))


infile.close()