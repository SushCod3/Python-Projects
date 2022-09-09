
# This Program lets you search a month of specific year or even a whole year.

import calendar

print('\nCALDENDAR\n')
x = calendar.TextCalendar()


def search_calendar():
    choose = input('Whole Year (y)\nSpecific Month (m)\n: ')
    if choose.lower() == 'y'.lower():
        year = int(input('\nEnter the year: \n: '))
        print(x.pryear(year))
    elif choose.lower() == 'm'.lower():
        month = int(input('\nEnter the month: \n: '))
        year = int(input('\nEnter the year: \n: '))
        print(f'\n{calendar.month(year, month)}')


search_calendar()
