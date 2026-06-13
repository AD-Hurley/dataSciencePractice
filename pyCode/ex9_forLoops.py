result = ["heads","tails","tails","heads","tails","heads","heads","tails","tails","tails"]

numHead=0

for i in result:
    if i=="heads":
        numHead+=1

print('The number of heads was '+str(numHead))

for i in range(11):
    if i%2!=0:
        print(i)

print()

expense_list = [2340, 2500, 2100, 3100, 2980]
print(len(expense_list))

usrInput = int(input('Enter an amount: '))
if usrInput in expense_list:
    for i in range(len(expense_list)):
        if usrInput == expense_list[i]:
            print('You spent '+str(usrInput)+' in month #'+str(i+1))
            break
else:
    print('You did not spend that exact amount during any month on record')

for i in range(1,5):
    usrInput = input("You've ran "+str(i)+'km. Are you tired? (yes or no):')
    if usrInput == 'yes':
        print('You did not finish the race')
        break
    elif usrInput == 'no' and i == 4:
        print('You finished the race')

starStr=''
for i in range(1,6):
    starStr=starStr+'*'
    print(starStr)