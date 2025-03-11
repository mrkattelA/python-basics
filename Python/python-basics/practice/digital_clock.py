import time

def set_clock():
    print("Starting Clock")
    try:
        while True:
            localtime = time.localtime()
            result = time.strftime(" %I:%M:%S %p", localtime)
            print(result)
            time.sleep(1)
    except KeyboardInterrupt:
        print("Stoping Clock")

set_clock()