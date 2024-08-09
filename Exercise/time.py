import time
# b = time.strftime("%H:%M:%S:%p")
# strftime is used to get the current hour of the day from the system's time
a = time.strftime('%I') 
hour = int(time.strftime('%H'))
minute = int(time.strftime('%M'))
second = int(time.strftime('%S'))
am = time.strftime('%p')
print("Hello Sir It's ",)
print( hour, minute , second , am , sep=":")
if( hour >= 5 and hour <= 12 ):
    print("And Good Morning,\nHave a Nice Day.")
elif( hour >= 13 and hour <= 17 ):
    print('Good Afternoon Sir')
elif( hour  >= 18  and hour <= 20 ):
    print("Good Evening Sir")
else:
    print('Good Night Sir')

# https://docs.python.org/3/library/time.html#time.strftime

