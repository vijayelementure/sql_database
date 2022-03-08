from calendar import month
import datetime
from locale import DAY_1

current_date = datetime.datetime.now()
print("current date :",current_date)
month=2
new_date = current_date + datetime.timedelta(days=3)
print("new_date     :  ",new_date)


