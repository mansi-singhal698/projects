# create a python program capable of geeting you with Good Morning , Good Afternoon and Good Evening , Your program should use time module to get the current hour.
import time
timestarp = time.strftime('%H:%M:%S')
hour = int(time.strftime('%H'))
print(hour)

if(hour>=0 and hour<12):
    print("good morning")
elif(hour>=12 and hour<17):
    print("good afternoon")
elif(hour>=17 and hour<0):
    print("good night")
