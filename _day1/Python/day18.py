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






print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

choice = (input("Enter choice: "))

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

if choice == 1:
    print("Answer =", a + b)

elif choice == 2:
    print("Answer =", a - b)

elif choice == 3:
    print("Answer =", a * b)

elif choice == 4:
    print("Answer =", a / b)

else:
    print("Invalid choice")