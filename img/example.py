import datetime

def gettime():
    now = datetime.datetime.now()

    return now.hour, now.minute, now.second + 1e-6 * now.microsecond

# get the time
hour, minute, seconds = gettime()

print(f"The current time is {hour}:{minute}:{seconds}")