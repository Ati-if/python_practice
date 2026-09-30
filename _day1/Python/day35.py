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





sentence = input("Enter a sentence: ")

words = sentence.split()
print("The number of words in the sentence is:", len(words))

# Define vowels
vowels_list = "aeiouAEIOU"

# Filter vowels and consonants using list comprehensions
vowels = [char for char in sentence if char in vowels_list]
consonants = [char for char in sentence if char.isalpha() and char not in vowels_list]

print("Vowels found:", vowels)
print("Number of vowels:", len(vowels))

print("Consonants found:", consonants)
print("Number of consonants:", len(consonants))