cat_age = input('How old is your cat? ')

cat_age = int(cat_age)
if cat_age >= 0: #cat is alive
    if cat_age < 2:
        print('What a cute kitten')
    elif cat_age < 9:
        print('What a medium aged cat')
        if cat_age == 7:
            print('7 is a lucky number')
    else:
        print('Your cat is old as hell')