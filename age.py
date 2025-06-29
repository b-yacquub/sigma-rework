# age
from datetime import date
today = date.today()

print(today)


def age():
    birthdate = input('enter you dob in the format dd-mm-yyyy')
    print(int(birthdate[6:]))
    age = today.year - int(birthdate[6:])
    if today.month < int(birthdate[3:5]):
        age = age - 1
        return age
    elif today.month == int(birthdate[3:5]) and today.day < int(birthdate[:2]):
        age = age - 1
        return age
    else:
        return age


print(age())
