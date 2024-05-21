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
