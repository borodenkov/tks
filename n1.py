import csv
import datetime


time_max = datetime.datetime.strptime('2016.09.11', '%Y.%m.%d')
time_old = datetime.datetime.strptime('2016.09.11', '%Y.%m.%d')

with open('data', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
    print(spamreader)
    for row in spamreader:
        time = datetime.datetime.strptime(row[1], '%Y.%m.%d')
        if time_old > time:
            print(row[0],row[1],time,time_max)
        elif time_max < time:
            time_max = time
        time_old = time
