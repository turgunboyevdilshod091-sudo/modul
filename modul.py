import math as m
print(m.sqrt(25))

import random
son=[1,7,8,9,5,6,4,6,5]
print(random.choice(son))

from datetime import date,datetime,timedelta
today=date.today()
birthday=date(2008,12,12)
delta = today - birthday
print(delta.days)