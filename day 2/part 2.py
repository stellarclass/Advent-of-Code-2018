fabric = []

with open('input.txt') as file:
    for line in file:
        line = line.strip()
        fabric.append(line)
       
linenum = 0
for line in fabric:
    A = line
    for line in fabric:
        if line == A:
            break
        else:
            j = 0
            temp = 0
            for j in range(len(line)):
                if A[j] == line[j]:
                    continue
                elif A[j] != line[j]:
                    temp += 1

                j += 1
            
            if temp == 1:
               print(A)
               print(line)