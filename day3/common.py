in_file = open('input.txt', 'r')
in_lines = in_file.readlines()
line_count = len(in_lines)
line_len = len(in_lines[0].strip())
lines = (list(line.strip()) for line in in_lines)
counts = {i:0 for i in range(line_len)}
for line in lines:
    for i in range(len(line)):
        if line[i] == "1":
            counts[i] += 1
result = "".join(("1" if counts[i] > line_count / 2 else "0" for i in range(line_len)))
flipped_result = "".join(("1" if i == "0" else "0" for i in result)) 
print(int(result, 2) * int(flipped_result, 2))
