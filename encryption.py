import random
import string

chars = " " + string.punctuation + string.digits + string.ascii_letters

chars = list(chars)
key = chars.copy()


random.shuffle(key)

print(f"chars: {chars} " )
print(f"key: {key}")

#ENCRYPT
plain_text = input("Enter some message to encrypt:")
cypher_text = ""

for letter in plain_text:
        index = chars.index(letter)
        cypher_text += key[index]

print(f"Original message: {plain_text}")
print(f"Encrypted message: {cypher_text}") 