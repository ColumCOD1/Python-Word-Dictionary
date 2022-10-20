# havea python dictionary that has a key/value pair that represents a word and it's definition
# collect input from the user, input is a word 
# check if the word is within the dictionary
# print that 

from PyDictionary import PyDictionary

dictionary = PyDictionary()

while True:
    word = input("Enter your word: ")
    if word == "":
        break 

    print(dictionary.meaning(word))
#def main():
   # word_dictionary = {
        #'hi': 'a way to greet someone',
        #'eyes': 'an organ for seeing and identifying objects or places',
        #'earth': 'a planet in our solar system'
    #}
    #while True:
       # word =input("Enter a word: ")
        #if word == "":
            #break
        #if word in word_dictionary:
            #print(word, ":", word_dictionary[word])

#main()
