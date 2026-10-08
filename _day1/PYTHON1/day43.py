print("Hello, World!")






number = int(input("Enter some numbers :"))

if number > 0 :
    print(number , "is a positive number")

elif number < 0 :
    print(number , "is a negative number")

else :
    print(number , "is zero")










numbers = [10 , 20 , 30 , 40 , 50 , 60]

total = 0

for number in numbers :
    total += number


print("The sum of all numbers in the list is :" , total)











password = input("Enter a password :")

if len(password) < 5 :
    print("Password is too short")

elif len(password) > 10 :
    print("Password is too long")

else :
    print("Password is valid")









password = input("Enter a password :")

if password.isalnum() and len(password) >= 5 and len(password) <= 10 :
    print("Password is valid")

elif not password.isalnum() :
    print("Password should contain only letters and numbers")

else :
    print("Password should be between 5 and 10 characters long")











number = int(input("Enter a number :"))

factorial = 1

for i in range(1 , number + 1) :
    factorial *= i

print("The factorial of" , number , "is :" , factorial)









number = int(input("Enter a number : "))

# Store the original value so it can be printed later
original_number = number

count = 0

# Handle 0 specifically since a 0 input has 1 digit
if number == 0:
    count = 1
else:
    # Use absolute value to support negative numbers
    number = abs(number)
    while number > 0:
        number //= 10  # Equivalent to number = number // 10
        count += 1

print(f"The number of digits in {original_number} is : {count}")












def check_palindrome(string):
    # Remove spaces and convert to lowercase for uniformity
    cleaned_string = string.replace(" ", "").lower()
    # Check if the cleaned string is equal to its reverse
    return cleaned_string == cleaned_string[::-1]


result = check_palindrome("racecar")

print(result)









def check_palindrome(string):
    # Remove spaces and convert to lowercase for uniformity
    cleaned_string = string.replace(" ", "").lower()
    # Check if the cleaned string is equal to its reverse
    return cleaned_string == cleaned_string[::-1]

# Example usage / Testing the function
test_strings = [
    "racecar",
    "A man a plan a canal Panama",
    "hello",
    "Never odd or even",
    "Python"
]

for s in test_strings:
    print(f"'{s}' -> {check_palindrome(s)}")









import string

def check_palindrome_advanced(text):
    # Keep only alphanumeric characters (letters and digits) and convert to lowercase
    cleaned_string = "".join(char.lower() for char in text if char.isalnum())
    return cleaned_string == cleaned_string[::-1]

# Example with punctuation
print(check_palindrome_advanced("A man, a plan, a canal: Panama!")) # Returns True











total = 0 

for i in range(1 , 86) :
    if i % 2 != 0 :
        total += i

print("The sum is :" , total)
