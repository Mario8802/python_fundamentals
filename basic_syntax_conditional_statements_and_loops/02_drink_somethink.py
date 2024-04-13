def persons_age(age: int) -> str:
    if age <= 14:
        return "drink toddy"
    elif age <= 18:
        return "drink coke"
    elif age < 21:
        return "drink beer"
    elif age >= 21:
        return "drink whisky"


age_customer = int(input())

print(persons_age(age_customer))
