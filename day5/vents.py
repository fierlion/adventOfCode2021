from collections import namedtuple
from collections import defaultdict

def add_all_vent_points(start, end, is_vert, points_counter):
    this_point = None
    if is_vert:
        for i in range(start.y, end.y+1):
            this_point = Point(start.x, i)
            points_counter[this_point] += 1
    else:
        for i in range(start.x, end.x+1):
            this_point = Point(i, start.y)
            points_counter[this_point] += 1

in_file = open('input.txt', 'r')
in_lines = in_file.readlines()
stripped_lines = [line.strip().split("->") for line in in_lines]
vents = []
vent_counter = defaultdict(int) 
Point = namedtuple('Point', 'x y')
for line in stripped_lines:
    this_start = line[0].strip().split(',')
    start_point = Point(int(this_start[0]), int(this_start[1]))
    this_end = line[1].strip().split(',')
    end_point = Point(int(this_end[0]), int(this_end[1]))
    vents.append((start_point, end_point))
# only vert/horiz lines
filtered_vents = list(filter(lambda x: ((x[0].x == x[1].x) or (x[0].y == x[1].y)), vents))
# add each line to vent_points and count collisions
for vent in filtered_vents:
    if vent[0].x == vent[1].x:
        start, end = (vent[0], vent[1]) if vent[0].y <= vent[1].y else (vent[1], vent[0])
        add_all_vent_points(start, end, True, vent_counter)
    else:
        start, end = (vent[0], vent[1]) if vent[0].x <= vent[1].x else (vent[1], vent[0])
        add_all_vent_points(start, end, False, vent_counter)

print(len(list(filter(lambda x: x > 1, vent_counter.values()))))
