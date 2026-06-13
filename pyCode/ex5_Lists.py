print('1)')
janExpense=2200
febExpense=2350
marExpense=2600
aprExpense=2130
mayExpense=2190

monthlyExpenses=[janExpense,febExpense,marExpense,aprExpense,mayExpense]
print(monthlyExpenses)

threeMonthExpense=monthlyExpenses[0]+monthlyExpenses[1]+monthlyExpenses[2]
print('Total expenses for the first three months: '+str(threeMonthExpense))

if(monthlyExpenses.__contains__(2000)):
    print("yes, You spent exactly 2000 in a month")
else:
    print("no, you did not spent exactly 2000 in a month")

juneExpense=1980

monthlyExpenses.append(juneExpense)
print(monthlyExpenses)

monthlyExpenses[3]=monthlyExpenses[3]-200
print(monthlyExpenses)
print()

print('2)')
heros=['spider man','thor','hulk','iron man','captain america']
print(len(heros))
print(heros)
heros.append('black panther')
print(heros)
heros.remove('black panther')
print(heros)
heros.insert(3,'black panther')
print(heros)
heros[1:3]=['doctor strange']
print(heros)
heros.sort()
print(heros)