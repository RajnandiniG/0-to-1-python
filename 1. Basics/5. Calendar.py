import calendar
text_cal=calendar.TextCalendar()
#To set first day as Sunday
text_cal.setfirstweekday(calendar.SUNDAY)
#Print calendar
text_cal.prmonth(2026,12)

#Display calendar in shell type...
#$ python -m calendar
#$ python -m calendar 2054 12
