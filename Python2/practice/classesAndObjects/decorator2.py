from datetime import datetime

def format_report(f):
    def inner(text):
        print("My Report")
        print('-' * 50)
        f(text)
        print('-' * 50)
        print("Report Completed: {}.".format(datetime.now()))
    return inner

def report(text):
    print(text)

report = format_report(report)

report("I have created my first decorator")
    