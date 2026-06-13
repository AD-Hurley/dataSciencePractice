usrInput = input('Enter your blood sugar level: ')
if float(usrInput) < 80:
    print('Your blood sugar is lower than normal')
elif float(usrInput) < 100:
    print('Your blood sugar is a normal level')
else:
    print('Your blood sugar is higher than normal')