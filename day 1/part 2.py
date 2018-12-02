frequency = []

with open('input.txt') as file:
    for line in file:
        line = line.strip()
        frequency.append(line)

start = 0
j = 0
freq = {0 : True}
while True:
     start += int(frequency[j])
     if start in freq:
         print("duplicate:")
         print(start)
         break
     else:
         freq[start] = True
     j += 1
     if j == len(frequency):
     	j = 0
file.close()