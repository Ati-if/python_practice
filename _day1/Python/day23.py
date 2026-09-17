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







r = int(input("Enter the number of rows: "))
c = int(input("Enter the number of columns: "))
x = []
for i_row in range(r):
    val = []
    for j_col in range(c):
        element = int(input(f"Enter the {i_row + 1} * {j_col + 1} element: "))
        val.append(element)
    x.append(val)

y = []
for i_row in range(r):
    val = []
    for j_col in range(c):
        element = int(input(f"Enter the {i_row + 1} * {j_col + 1} element: "))
        val.append(element)
    y.append(val)

sum_matrix = []
for i_row in range(r):
    val = []
    for j_col in range(c):
        val.append(x[i_row][j_col] + y[i_row][j_col])
    sum_matrix.append(val)

print(sum_matrix)