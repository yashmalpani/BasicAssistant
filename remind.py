import datetime
import os
import csv
import reminder
import time


while True:
    with open('reminders.csv') as f:
        reader = csv.reader(f)
        now = datetime.datetime.now()
        reminders = [row[1].strip() for row in reader if datetime.datetime.strptime(row.strip(',')[0][1:],'%Y-%m-%d-%H:%M:%S') <= now]
        no_of_rem = len(reminders)
        if no_of_rem > 0:
            reminder.delete()
            for i in reminders:
                os.system('notify-send "Reminder : ' + i + '"')
        else:
            time.sleep(60)