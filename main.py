
import datetime
import os

alarm_hour = int(input("Set hour: "))
alarm_minutes = int(input("Set minute: "))

print(f"Waiting for time to alarm: {alarm_hour}.{alarm_minutes}")

while True:
    if alarm_hour == datetime.datetime.now().hour and alarm_minutes == datetime.datetime.now().minute :
        print("WAKE UP!!")
        os.system("start Padisah.mp4")
        break