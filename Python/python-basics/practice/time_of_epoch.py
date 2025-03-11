import time

second_since_epoch = time.time()
minutes_since_epoch = second_since_epoch/60
hours_since_epoch = minutes_since_epoch/60
days_since_epoch = hours_since_epoch/24
year_since_epoch = days_since_epoch/365.25

print(""" The Current Total Since Epoch
Seconds: {: ,.2f}
minutes:{: ,.2f}
hours:{: ,.2f}
days{: ,.2f}
year{: ,.2f}""".format(second_since_epoch,minutes_since_epoch,
                   hours_since_epoch,days_since_epoch,
                   year_since_epoch)            )