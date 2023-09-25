import math
import os
import random
import re
import sys


integer = int(input())
    

if integer % 2 != 0:
        print("Weird")
    
else:
    if integer in range(2, 5):
            print("Not Weird")

    elif integer > 20:
        print("Not Weird")

    elif integer in range(6, 20):
        print("Weird")

