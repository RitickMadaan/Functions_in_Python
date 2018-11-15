minutes=int(input("Please enter the number of minutes: "))
seconds=int(input("Please enter the number of seconds: "))
def minutes_to_hours(minutes):
    hours = (minutes/60)
    return hours
def seconds_to_hours(seconds):
    hours=(seconds/3600)
    return hours
print(minutes_to_hours(minutes)+seconds_to_hours(seconds))
