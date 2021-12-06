in_file = open('input.txt', 'r')
lines = in_file.readlines()
int_lines = [int(line) for line in lines]

window_size = 3
count = 0
current = 0
for i in range(len(int_lines) - window_size + 1):
    summed = sum(int_lines[i : i + window_size])
    print(summed)
    if summed > current:
        count += 1
    current = summed
print(count)
