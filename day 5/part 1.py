polymer = []
react = []

with open('input.txt') as file:
    for line in file:
        line = line.strip()
        for char in line:
            polymer.append(char)

#my input has the first two reacting, so there's probably an elegant way to address it but i am not good at code
react.append(polymer[0])
polymer.pop(0)
react.append(polymer[0])
polymer.pop(0)
react.append(polymer[0])
polymer.pop(0)

react.pop(0)
react.pop(0)

for x in range(len(polymer)):
        if react[-1] == polymer[x].swapcase():
            react.pop(-1)
        else:
            react.append(polymer[x])
    
print(len(react))
