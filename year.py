def is365(year):
    if year%400==0 or year%4==0:
        return 'True';
    else:
        return 'False';
year = int(raw_input('input year:'))
print is365(year)