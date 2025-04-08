def days_of_week(day):
    match day:
     case 1:
        return "It is Sunday"
     case 2:
        return "It is Monday"
     case 3:
        return "It is Tuesday"
     case 4:
        return "It is Wednesday"
     case 5:
        return "It is Thursday"
     case 6:
        return "It is Friday"
     case 7:
        return "It is Saturday"
     case _:
        return "Invalid day number"

print(days_of_week(2))