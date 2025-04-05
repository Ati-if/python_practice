def add(a , b):
    
    return a + b

print(add(2 , 3)) 






def add(*args):
    print(type(args))

add(1 , 2 , 3) 








def add(*args):
    total = 0
    for arg in args:
      total += arg
    return total

print(add(1 , 2 , 3 , 4))