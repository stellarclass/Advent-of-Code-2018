frequency = []

with open('input.txt') as file:
    for line in file:
        line = line.strip()
        frequency.append(line)
        
frequency.extend(frequency)
frequency.extend(frequency)
frequency.extend(frequency)
frequency.extend(frequency)
frequency.extend(frequency)
frequency.extend(frequency)
frequency.extend(frequency)
frequency.extend(frequency)


start = 0
freq = []

for line in frequency:
     start += int(line)
     if start in freq:
         print("duplicate:")
         print(start)
         break
     else:
         freq.append(start)
file.close()