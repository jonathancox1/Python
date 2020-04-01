#prompt the user for their name
name = input('Whats your name? ')


#convert their name to uppercase
upper_name = name.upper()
name_len = len(name)


#print their name with hello and the amoount of letters in their name
print(f'Hello, {upper_name}')
print(f'Your name has {name_len} letters in it')