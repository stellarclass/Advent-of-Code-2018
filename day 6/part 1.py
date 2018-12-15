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

for index, values in np.ndenumerate(box):
    boxind = []
    for j in range(len(coords)):
        xtaxi = abs(index[0] - coords[j, 0])
        ytaxi = abs(index[1] - coords[j, 1])
        taxicab = xtaxi + ytaxi
        boxind.append(taxicab)
    if boxind.count(min(boxind)) > 1:
        box[index] = -1
    else:
        box[index] = boxind.index(min(boxind))

ignorelist = []
for index, values in np.ndenumerate(box):
    if  index[0] == 0 or index[1] == 0 or index[0] == box.shape[0]-1 or index[1] == box.shape[1]-1:
        ignorelist.append(values)

ignorelist = set(ignorelist)

unique, counts = np.unique(box, return_counts = True)
area = dict(zip(unique, counts))

for j in ignorelist:
    area.pop(j)

key = max(area, key = area.get)
print(area[key])
