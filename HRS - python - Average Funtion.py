#!/bin/python3

import math
import os
import random
import re
import sys


# write your code here
nums = list(map(int, input().split()))
s=0
l=0
for i in nums:
    s=s+i
    l=l+1
r=s/l
f=float(r)
print(format(r, ".2f"))