import calendar
text_cal=calendar.TextCalendar()
#To set first day as Sunday
text_cal.setfirstweekday(calendar.SUNDAY)
#Print calendar
text_cal.prmonth(2026,12)

#Display calendar in shell type...
#$ python -m calendar
#$ python -m calendar 2054 12
```````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````
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
```````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````
#Car game
import time
# Initial message
print("Let's get started...")
# Introduce a delay of 1 seconds
time.sleep(1)
def car_game():
    while True:
        user_input = input("Provide input: ").lower()

        if user_input == 'help':
            print("start: to start the car \nstop: to stop the car \nquit: to exit")
        elif user_input == 'start':
            print("Car started... Ready to go!")
        elif user_input == 'stop':
            print("Car stopped.")
        elif user_input == 'quit':
            print("Exiting the game. Goodbye!")
            break
        else:
            print("I don't understand")
# Start the game
car_game()
