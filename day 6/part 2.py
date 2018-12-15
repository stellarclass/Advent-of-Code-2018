import numpy as np

coords = []

with open('input.txt') as file:
    for line in file:
        line = line.strip()
        line = line.split(", ")
        coords.append(line)
        
coords = np.asarray(coords)
coords = coords.astype(np.int)

xymax = np.amax(coords, axis = 0)
xymin = np.amin(coords, axis = 0)

box = np.zeros(xymax - xymin)

coords -= xymin
area = 0

for index, values in np.ndenumerate(box):
    distance = 0
    for j in range(len(coords)):
        xtaxi = abs(index[0] - coords[j, 0])
        ytaxi = abs(index[1] - coords[j, 1])
        taxicab = xtaxi + ytaxi
        distance += taxicab
    if distance < 10000:
        area += 1

print(area)