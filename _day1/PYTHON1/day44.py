print("This is Atif , day44 of python practice .")






print("Testing my skills in python language .")









for number in range(2 , 51) :
    even = True

    for i in range(2 , number) :
        if number % 2 != 0 :
            even = False
            break

    if even :
        print(number)