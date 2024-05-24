import calendar
text_cal=calendar.TextCalendar()
#To set first day as Sunday
text_cal.setfirstweekday(calendar.SUNDAY)
#Print calendar
text_cal.prmonth(2026,12)

#Display calendar in shell type...
#$ python -m calendar
#$ python -m calendar 2054 12

#Now let's try to build a guessing game, where user will be given 3 chance to guess a secret number.
secret_no=11
guess_count=1
while guess_count<3:
    guess_no=int(input(f"Guess {guess_count}: "))
    guess_count +=1
    if guess_no==secret_no:
        print('You won!!!')
        break #If user guess it right, will break the loop
    else:
        print('Try again!')
else:
    print('No more guess left!')
