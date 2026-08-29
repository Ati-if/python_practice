word = input("Enter a word: ")

if word.startswith("A"):
    print("The word starts with A")
else:
    print("The word does not start with A")





word = input("Enter a word: ")

if word.endswith("ing"):
    print("The word ends with ing")
else:
    print("The word does not end with ing")







sentence = input("Enter a sentence: ")

new_sentence = sentence.replace("bad", "good")

print(new_sentence)