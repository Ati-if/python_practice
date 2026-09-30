text = input("Enter a word :")

vowels = 0
consonants = 0

for letter in text :
    if letter in "aeiouAEIOU" :
        vowels += 1
    elif letter.isalpha() :
        consonants += 1


print("Number of vowels in the word is :" , vowels)
print("Number of consonants in the word is :" , consonants) 





sentence = input("Enter a sentence :")

words = sentence.split()

print("The number of words in the sentence is :" , len(words))