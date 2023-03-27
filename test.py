import datetime

current_date = datetime.datetime.now()
yesterday = current_date - datetime.timedelta(weeks=1)

print(current_date, type(current_date))
print(yesterday)
