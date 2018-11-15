min=int(input("Please enter the number of minutes: "))
#sec=int(input("Please enter the number of seconds: "))
def hours(minutes,seconds=60):
    hours=minutes/60 + seconds/3600
    print(hours)
hours(min)
