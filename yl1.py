from __future__ import print_function
f = open('input1.txt')
contents = f.read()
print("Floor:", contents.count('(') - contents.count(')'))
# part2
change = {'(': 1, ')': -1}

floor = 0
position = 1
for c in contents:
    if c in change:
        floor += change[c]
    if floor == -1:
        print("Basement entered at position:", position)
        break
    position += 1
