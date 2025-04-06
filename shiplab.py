def shipping_label(*args , **kwargs):
    for arg in args:
        print(arg, end=" ")
    print()
    for value in kwargs.values():
        print(value, end=" ")



shipping_label("Dr.", "Spongebob", "Squarepants", "II" ,
               street = "123 fake st.",
               apt = "100",
               city = "Detroit")