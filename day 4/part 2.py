import pandas as pd
import numpy as np
from datetime import datetime as dt
from datetime import timedelta as td

def after(value, a):
    # Find and validate first part.
    pos_a = value.rfind(a)
    if pos_a == -1: return ""
    # Returns chars after the found string.
    adjusted_pos_a = pos_a + len(a)
    if adjusted_pos_a >= len(value): return ""
    return value[adjusted_pos_a:]

def before(value, a):
    # Find first part and return slice before it.
    pos_a = value.find(a)
    if pos_a == -1: return ""
    return value[0:pos_a]

guards = []

with open('input.txt') as file:
    for line in file:
        line = line.strip()
        guards.append(line)
                
#guards = ["[1518-11-03 00:29] wakes up",
#          "[1518-11-04 00:02] Guard #99 begins shift",
#          "[1518-11-05 00:45] falls asleep",
#          "[1518-11-05 00:55] wakes up",
#          "[1518-11-03 00:24] falls asleep",
#          "[1518-11-01 00:25] wakes up",
#          "[1518-11-01 00:30] falls asleep",
#          "[1518-11-01 00:55] wakes up",
#          "[1518-11-01 23:58] Guard #99 begins shift",
#          "[1518-11-04 00:36] falls asleep",
#          "[1518-11-01 00:00] Guard #10 begins shift",
#          "[1518-11-01 00:05] falls asleep",
#          "[1518-11-02 00:40] falls asleep",
#          "[1518-11-02 00:50] wakes up",
#          "[1518-11-03 00:05] Guard #10 begins shift",
#          "[1518-11-04 00:46] wakes up",
#          "[1518-11-05 00:03] Guard #99 begins shift",]

guards.sort()

wakestate = []
date = []
time = []
guard = []
j = 0

for line in guards:
    line = line.split(" ", maxsplit = 2)
    
    x = (after(line[0], "["))
    y = (before(line[1], "]"))
    
    if y.find("23:") != -1:
        x = before((str(dt.strptime(x, "%Y-%m-%d") + td(days=1))), " ")
        y = "00:00"
        
    date.append(x)
    time.append(y)
    
    if line[2].find("#") != -1:
           guard.append(before(after(line[2], "#"), " begins"))
           wakestate.append("awake")
    if line[2].find("asleep") != -1:
            wakestate.append("sleeping")
            guard.append(guard[j-1])
    if line[2].find("wakes") != -1:
            wakestate.append("awake")
            guard.append(guard[j-1])
    j += 1

colname = []

for var in guard:
    if var not in colname:
        colname.append(var)

df = pd.DataFrame(np.zeros((60, len(colname))), columns = colname)

for i in range(len(time)):
    g = guard[i]
    print(g)
    if wakestate[i] == "sleeping":
        x = int(after(time[i], ":"))
        y = int(after(time[i+1], ":"))
        while x != y:
            df.loc[x, g] += 1
            x += 1
        
print(df.values.max())

print(51*1901)
