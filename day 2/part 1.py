checksum = []

with open('input.txt') as file:
    for line in file:
        line = line.strip()
        checksum.append(line)

linenum2 = 0
linenum3 = 0
j = 0

for line in checksum:
    j += 1
    chars = dict()
    for ch in line:
        if ch not in chars:
            chars[ch] = 1
        else:
            chars[ch] += 1
    for x in chars:
        if chars[x] == 2:
            linenum2 += 1
            break
    for x in chars:
        if chars[x] == 3:
            linenum3 += 1
            break
        
print(linenum2)
print(linenum3)        
print(linenum2 * linenum3)