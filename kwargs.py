def print_adress(**kwargs):
    
    print(type(kwargs))

print_adress(street="123 fake St.",
                     city = "Detroit")







def print_adress(**kwargs):
    for value in kwargs.values():
        print(value)


print_adress(street="123 fake St.",
                     city = "Detroit")                    