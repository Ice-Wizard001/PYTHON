import time
timestamp=time.strftime('%H:%M:%S')
print(timestamp)

timestamp1=int(time.strftime('%H'))

if timestamp1 <12:
    print("Good Morning Sir")

elif 12<= timestamp1 <17:
    print("Good Afternoon")

elif 17<= timestamp1 <20:
    print("Good Evening")

else:
    print("Good Night")