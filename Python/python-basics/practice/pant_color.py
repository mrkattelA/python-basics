from datetime import datetime

def is_summer(the_date=datetime.now()):
    year = the_date.year

    summer_start=datetime(year,6,20)
    fall_start= datetime(year,9,22)
    return (summer_start<the_date<fall_start)

def main():
    y = int(input("Enter the year: "))
    m = int(input("Enter the month: "))
    d = int(input("Enter the day: "))
    date_time = datetime(y,m,d)
    pant_color = "white" if is_summer(date_time) else "black"
    print(f"you should wear {pant_color} pants on {date_time.strftime("%a %B %d, %Y.")} ")

main()
