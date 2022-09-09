# Leap Year Checker

def leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                print(f'Year {year} is a Leap Year!')
            else:
                print(f'Year {year} is not a Leap Year.')
        else:
            print(f'Year {year} is a Leap Year!')
    else:
        print(f'Year {year} is not a Leap Year.')


while True:
    user = int(input('Enter the year: '))
    leap_year(user)
