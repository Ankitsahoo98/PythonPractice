# print today's date
# print yesterday's date
# ask a user to enter a date
# print the date one week from the date entered
from datetime import datetime,timedelta
today = datetime.now()
print("Today's date is: " + str(today))
one_day = timedelta(days=1)
yesterday = today - one_day
print("Yesterday's date was: "+str(yesterday))
exam = input('The exam date is(dd/mm/yyyy) : ')
exam_date = datetime.strptime(exam, '%d/%m/%Y')
one_week = timedelta(weeks=1)
af_one_week = exam_date + one_week
print('The date after one week of your exam : '+str(af_one_week))
