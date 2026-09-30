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











total_sales = 0

for i in range(1 , 3) :
    sales = float(input("Enter the sales for employee  {i} :"))

    if sales < 5000 :
        tax = sales * 0.05
    elif sales < 10000 :
        tax = sales * 0.10
    else :
        tax = sales * 0.15

    print(f"The tax for employee {i} is :" , tax)
    print(f"The sales of employee {i} is :" , sales)
    print("-"  * 20)

    total_sales += sales 

average_sales = total_sales / 5

print("Total sales : RS ."  , round(total_sales , 2))
print("Average_sales : RS. " , round(average_sales , 2))








class Customer :
    def __init__(self , name , customer_id) :
        self.name = name
        self.customer_id = customer_id


    def display_customer(self) :
        print("Customer Name: " , self.name)
        print("Customer ID :" , self.customer_id)


class Account :
    def __init__(self , account_number , customer , balance = 0) :
        self.account_number = account_number
        self.customer = customer
        self.balance = balance


    def deposit (self , amount) :
        if amount > 0 :
            self.balance += amount
            print(f"RS . {amount : .2f} deposited successfully ")
        else :
            print("Invalid deposit ammount")


    def withdraw(self , amount) :
        if amount <=  0 :
            print("Invalid withdrawl ammount .")
        elif amount > self.balance :
            print("Insufficient balance .")
        else :
            self.balance -= amount
            print(f"RS . {amount : .2f}  withdrawn successfully .")

    def display_balance(self) :
        print(f"Current balance is : RS . {self.balance : .2f}")


customer1 = Customer("Ali" ,  "C001")

account1 = Account("A001" , customer1 , 10000)

customer1.display_customer()
print("Account_number :"  , account1.account_number)
print()

account1.display_balance()

account1.deposit(5000)
account1.display_balance()


account1.withdraw(3000)
account1.display_balance()





a = int(input("Enter a :"))
b = int(input("Enter b :"))


a , b = b , a 


print("a = " , a)
print("b =" , b)








numbers = [10 , 10 , 20 , 20 , 30 , 40 , 50]

unique = []

for number in numbers :
    if number not in unique :
        unique.append(number)


print(unique)