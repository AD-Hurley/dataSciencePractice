india = ["mumbai", "banglore", "chennai", "delhi"]
pakistan = ["lahore","karachi","islamabad"]
bangladesh = ["dhaka", "khulna", "rangpur"]

usrInput = input('Pleast enter a city: ')
if usrInput in india:
    print('This city is in India')
elif usrInput in pakistan:
    print('This city is in Pakistan')
elif usrInput in bangladesh:
    print('This city is in Bangladesh')
else:
    print("I don't know where that city is.")

usrInput = input('Pleast enter another city: ')
usrInput_2 = input('Enter another city: ')

if usrInput in india and usrInput_2 in india:
    print('Both cities are in India')
elif usrInput in pakistan and usrInput_2 in pakistan:
    print('Both cities are in Pakistan')
elif usrInput in bangladesh and usrInput_2 in bangladesh:
    print('Both cities are in Bangladesh')
else:
    print("Those cities are either not in the same city, or I don't know where that city is.")