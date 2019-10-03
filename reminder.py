import datetime
import csv
import operator

def set(year, month, day, hour, purpose):
    reminder_time = datetime.datetime(year, month, day, hour, minute=0, second=0, microsecond=0)
    row = [reminder_time.strftime('%Y-%m-%d-%H:%M:%S'),purpose]
    with open('reminders.csv','a') as f:
        writer = csv.writer(f)
        writer.writerow(row)
    with open('reminders.csv', 'r+') as fd:
        lines = fd.readlines()
        fd.seek(0)
        fd.writelines(line for line in lines if line.strip())
        fd.truncate()
    sort()



set(1910,10,10,10,10,'2000')
set(1910,10,10,10,10,'5000')
set(1920,10,10,10,10,'1000')
set(1910,6,10,10,10,'5000')




def sort():
    reader = csv.reader(open("reminders.csv"), delimiter=";")
    sortedlist = sorted(reader, key=operator.itemgetter(0), reverse=False)
    print(sortedlist)
    with open('reminders.csv','w') as f:
        writer = csv.writer(f)
        for i in sortedlist:
           writer.writerow(i)
    with open('reminders.csv', 'r+') as fd:
        lines = fd.readlines()
        fd.seek(0)
        fd.writelines(line for line in lines if line.strip())
        fd.truncate()

sort()

def delete():
    now = datetime.datetime.now()
    f = open('reminders.csv')
    a = f.readlines()
    count = 0
    for row in a:
        ts, pur = row.split(',')
        rem_time = datetime.datetime.strptime(ts[1:],'%Y-%m-%d-%H:%M:%S')
        if rem_time <= now:
            count += 1
        else:
            break
    actual = a[count:]
    f.close()
    with open('reminders.csv','w+') as fd:
        fd.writelines(line for line in actual)

delete()