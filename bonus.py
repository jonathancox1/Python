#prompt user for a number in days
days = input('Give me a number of days: ')

#convert the given amount of days into a variable 'seconds'
#dont forget to convert the users input into an integer
seconds = int(days) * 24 * 60 * 60


#determine if users input results in plural form of day/days
day_s = ''
if (int(days) > 1):
    day_s = 'days'
else:
    day_s = 'day'


#return the amount of seconds in the given number of day/days
print(f'There are {seconds} seconds in {days} {day_s}')



