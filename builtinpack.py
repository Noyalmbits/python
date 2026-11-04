import os
import sys
import json
import math
import random
import datetime
import time
print("\n1.OS module")
print("current directory:",os.getcwd())
print("operating system:",os.name)

print("\n2.SYS MODULE")
print("python version:",sys.version)
print("platform:",sys.platform)

print("\n3.JSON module")
data ={"name":"python","version":3.14}
json_data=json.dumps(data)
print("json:",json_data)
print("converted:",json.loads(json_data))

print("\n4.MATH module")
print("square root:",math.sqrt(64))
print("power:",math.pow(2,5))
print("factorial :",math.factorial(5))

print("\n5.RANDOM module")
print("random number:",random.randint(1,1000))
print("random choice:",random.choice(["apple","orange","banana"]))

print("\n6.DATETIME module")
now=datetime.datetime.now()
print("curent date and time:",now)
print("current year:",now.year)

print ("\n7.TIME module")
print("current Timestamp:",time.time())
print("formatted time:",time.ctime())

