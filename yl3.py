f = open('input3.txt')

def increment_house(x, y, houses):
    if (x, y) in houses:
        houses[(x, y)] += 1
    else:
        houses[(x, y)] = 1

def calc_move(x, y, move):
    if move == '^':
        y += 1
    elif move == 'v':
        y -= 1
    elif move == '>':
        x += 1
    else:
        x -= 1
    return x, y

santaX = 0
santaY = 0
houses = {}
increment_house(santaX, santaY, houses)
for char in data:
    santaX, santaY = calc_move(santaX, santaY, char)
    increment_house(santaX, santaY, houses)
print(len(houses))
