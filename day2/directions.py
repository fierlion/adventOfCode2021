in_file = open('input.txt', 'r')
lines = in_file.readlines()
line_tuples = (line.strip().split(' ') for line in lines)
position = (0, 0)
for update in line_tuples:
    distance = int(update[1])
    if update[0] == "forward":
        position = (position[0]+distance, position[1])
    elif update[0] == "down":
        position = (position[0], position[1]+distance)
    elif update[0] == "up":
        position = (position[0], position[1]-distance)
print(position[0] * position[1])
