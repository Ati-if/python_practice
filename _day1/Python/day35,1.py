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