def is_weekend(day):
    match day:
      case "Saturday" | "Sunday":
        return True
      case "Monday" | "Tuesday" | "Wednesday" | "Thursday" | "Friday":
        return False
      case _:
        return False

print(is_weekend("Saturday"))