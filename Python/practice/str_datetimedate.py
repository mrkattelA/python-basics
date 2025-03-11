import datetime

def str_datetime(date_time):
    date_parts = [int(i) for i in date_time.split("-")]
    return datetime.date(*date_parts)


str_date = input("Enter the date in format YYYY-MM-DD: ")


date = str_datetime(str_date)
print(date)
