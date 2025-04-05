def hello(Greeting , title , first_name , last_name):
    print(f"{Greeting} {title} {first_name} {last_name}")

hello("Hello" , "Mr" , "Atif" , "Nawaz")







def get_phone(country, area, first_name, last_name):
    return(f"{country}-{area}-{first_name}-{last_name}")

phone_num = get_phone(country=2, area=234, first_name=567, last_name=890)

print(phone_num)