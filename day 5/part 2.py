from string import ascii_lowercase

polymer = []
react = []
react2 = []

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

for c in ascii_lowercase:
    #wtf why are they linked python why
    react2 = list(react)
    for x in range(len(polymer)):
        if c == polymer[x].swapcase() or c == polymer[x]:
            continue
        elif react2[-1] == polymer[x].swapcase():
            react2.pop(-1)
        else:
            react2.append(polymer[x])
    print(str(c) + ": " + str(len(react2)))

#
#        
#for c in ascii_lowercase:
#    print(c)
#    polymer2 = []
#    react2 = []
#    
#    for y in react[c]:
#        polymer2.append(y)
#    
#    if c != "b":
#        react2.append(polymer2[0])
#        polymer2.pop(0)
#        react2.append(polymer2[0])
#        polymer2.pop(0)
#        react2.append(polymer2[0])
#        polymer2.pop(0)
#        react2.pop(0)
#        react2.pop(0)
#    else:
#        react2.append(polymer2[0])
#        polymer2.pop(0)
#    
#    print(react2)
#    for x in range(len(polymer2)):
#        if react2[-1] == polymer2[x].swapcase():
#            react2.pop(-1)
#        else:
#            react2.append(polymer2[x])
#    print(str(c) + ": " + str(len(react2)))
