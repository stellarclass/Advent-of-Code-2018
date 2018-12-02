frequency = open('input.txt')

start = 0

for line in frequency:
    start += int(line)
print(start)
frequency.close()