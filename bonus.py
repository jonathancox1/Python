#prompt user for a number in days
days = input('Give me a number of days: ')

#convert the given amount of days into a variable 'seconds'
#dont forget to convert the users input into an integer
seconds = int(days) * 24 * 60 * 60

#return the amount of seconds in the given days
print(f'There are {seconds} seconds in {days} day(s)')



