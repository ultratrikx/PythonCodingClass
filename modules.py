import random
import time
import calendar
import os
import urllib.request as req

num = random.randint(1, 100)
timeZone = time.tzname
calendar.prmonth(3021, 7)

print(num, timeZone)

for file in os.listdir(os.path.expanduser("~/Desktop/PythonCodingClass")):
    print(file)


myurl = "http://google.com"
data = req.urlopen(myurl).read()
print(data)


list1 = [1, 2, 3, 4, 5, 6]
print(random.choice(list1))

string = 'pythonstriver'
print(random.choice(string))

# prints list of random items of length 3 from the given list
print("With list:", random.sample(list1, 3))

# prints a random items of length 4 from the given string
print("With string:", random.sample(string, 4))
