import time
my_time = int(input("Enter the time in seconds: "))
for x in range(my_time, 0, -1):     #To reverse the timer
    seconds = x%60
    minutes = int(x/60)%60
    hours = int(x / 3600)
    print(f"{hours}:{minutes}:{seconds}")
    time.sleep(1)
print("TIME'S UP!")
