# what we import from extra operation
#math — for mathematical functions
import math

print(math.sqrt(25))
print(math.pi)
#random — to generate random numbers
import random

print(random.randint(1,10))
#datetime — for dates and time
import datetime

print(datetime.datetime.now())
#os — to work with files & folders
import os

print(os.listdir())
#sys — for system-related functions
import sys

print(sys.version)
#numpy — for arrays & math (external library)
import numpy as np
arr = np.array([1,2,3])
#pandas — for data analysis (external library)
import pandas as pd
| Task                          | Module to Import |
| ----------------------------- | ---------------- |
| Random numbers                | random           |
| Square root, pi, trigonometry | math             |
| Date & time                   | datetime         |
| Files, folders                | os               |
| Advanced math arrays          | numpy            |
| Data analysis & tables        | pandas           |
| API requests                  | requests         |
| JSON data                     | json             |
'''Only import a module when you need special functionality.
Python will tell you if something is missing.'''



