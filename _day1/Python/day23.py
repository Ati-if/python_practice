stg1 = "Hello"
stg2 = "World"
stg3 = stg1 + " " + stg2
print(stg3)





stg1 = "Hey"
stg2 = "there"
stg3 = "All"
stg = " {} {} , {}! ".format(stg1, stg2, stg3)
print(stg)




d1 = {}
print(d1)
print(type(d1))






n = int(input("Enter a number: "))
for i in range (1 , n+1) :
    for j in range (1 , i+1) :
        print(j, end='')
    print()