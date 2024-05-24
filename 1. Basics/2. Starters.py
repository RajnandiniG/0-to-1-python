#Display calendar in shell type...
#$ python -m calendar
#$ python -m calendar 2054 12

#Build simple addition calculator
a = input('First number: ')
b = input('Second number: ')
print('Total:', float(a) + float(b))

#Calculate user's age
print('Check-In')
name = input('Enter your full name: ')
birth = input('Enter you birth year: ')
cal = 2024 - int(birth)
print('Your age is:', cal)

#Calculate weight
weight = float(input('Enter your Weight: '))
kl = input('Provided in K(k) kgs or L(l) lbs:')
if kl.lower() == 'k':
    print('Your weight in lbs:',(weight)*2.204) # 1 kg = 2.20462 lbs
elif kl.lower() == 'l':
    print('Your weight in kgs:',(weight)*0.45) # 1 lb = 0.453592 kg
else:
    print('Invalid input')

#Calculate down payment
price=1_000000
credit_score=False
if credit_score:
    print(f'Make a 10% payment:${0.1*price}')
else:
    print(f'Make 20% payment:${0.2*price}')
