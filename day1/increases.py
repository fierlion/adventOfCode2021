in_file = open('input.txt', 'r')
lines = in_file.readlines()
int_lines = [int(line) for line in lines]

window_size = 2
count = 0
for i in range(len(int_lines) - window_size + 1):
    if int_lines[i] < int_lines[i+1]:
        count += 1
print(count)
