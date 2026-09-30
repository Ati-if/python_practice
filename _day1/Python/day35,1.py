for i in range(1 , 11) :
    print(i , "="  , i * i * i)







for number in range(1 , 5) :
    print("Table of " , number)


    for i in range(1 , 11) :
        print(number , "x" , i , "=" , number * i)

print()










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