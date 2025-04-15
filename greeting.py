import time 

t = time.strftime('%H:%M %p')
hour = int(time.strftime('%H'))
minute = int(time.strftime('%M'))
print("The current time is =", t)


if (hour>=0 and hour<12):
    print("Good morning Sir !")
elif(hour>=12 and hour<17):
    print("Good afternoon Sir!")  
else:
    print("Good night Sir!")