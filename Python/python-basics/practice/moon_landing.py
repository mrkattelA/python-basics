import datetime
import time

moon_landing = datetime.datetime(year=1968,month=4,day=22,
                                 hour= 4,minute=44,second=22,
                                 tzinfo=datetime.timezone.utc)

print(moon_landing)
print("==========")

ml_anni = moon_landing.replace(year=1950)
print(ml_anni)