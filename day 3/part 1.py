import pandas as pd

fabric = []

with open('input.txt') as file:
    for line in file:
        line = line.strip()
        line = line.replace(" @ ", ",")
        line = line.replace(":", ",")
        line = line.replace("x", ",")
        fabric.append(line)

#fabric = ["#1, 1,3, 4,4",
#          "#2, 3,1, 4,4",
#          "#3, 5,5, 2,2"]
#print(fabric)

df1 = pd.DataFrame([sub.split(",") for sub in fabric])
df1.columns = ["ID", "X", "Y", "width", "height"]

df = df1.set_index("ID")
print(df)

coords = {}

for index, row in df.iterrows():
    x = int(row[0])
    y = int(row[1])
    xend = x + int(row[2]) - 1
    yend = y + int(row[3])
    xy = str(x)+","+str(y)
    xyend = str(xend)+","+str(yend)
   
    while xy != xyend:
        while y != yend:
            x = int(row[0])
            xy = str(x)+","+str(y)
            while x != xend:
                if xy not in coords:
                    coords[xy] = 1
                else:
                    coords[xy] += 1
                x += 1
                xy = str(x)+","+str(y)   

            if xy not in coords:
                coords[xy] = 1
            else:
                coords[xy] += 1
            y += 1
            xy = str(x)+","+str(y)
            

sqin = 0
for xy, value in coords.items():
    if coords[xy] > 1:
        sqin += 1
        
print(sqin)