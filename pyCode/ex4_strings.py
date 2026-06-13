print('1)')
street='Strasse'
city='Berlin'
country='Germany'

adress_1=street+" "+city+" "+country
adress_2=f'{street} {city} {country}'
print(adress_1)
print(adress_2)
print()

print('2)')
fact='Earth revolves around the sun'
print(fact)
print(fact[6:15])
print(fact[-3:])
print()

print('3)')
numDailyFruits=3
numDailyVeges=5
nutriFact=f"I eat {numDailyVeges} veggies and {numDailyFruits} fruits daily'"
print(nutriFact)
print()

print('4)')
s='maine 200 banana khaye'
#s=s[:6]+'10 samosa'+s[16:]
s=s.replace('banana','samosa').replace('200','10')
print(s)