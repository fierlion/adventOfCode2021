in_file = open('input.txt', 'r')
in_lines = in_file.readlines()
# we could do deepcopy here too -- but lazy
c02_lines = [list(line.strip()) for line in in_lines]
oxy_lines = [list(line.strip()) for line in in_lines]

input_size = len(c02_lines)
line_size = len(c02_lines[0])
c02_result = ""
oxy_result = ""

def common_bit_for_pos(arr_in, pos):
    ones_for_pos = sum((1 if line[pos] == '1' else 0 for line in arr_in))
    return '1' if ones_for_pos >= len(arr_in) / 2 else '0'

current_index = 0
for i in range(line_size):
    c02_common_bit = common_bit_for_pos(c02_lines, i)
    oxy_common_bit = common_bit_for_pos(oxy_lines, i)
    # mutuate the lines array
    c02_lines = list(filter(lambda x: x[i] == c02_common_bit, c02_lines))
    oxy_lines = list(filter(lambda x: x[i] != oxy_common_bit, oxy_lines))
    if len(c02_lines) == 1:
        c02_result = "".join(c02_lines[0])
        print(c02_result)
    if len(oxy_lines) == 1:
        oxy_result = "".join(oxy_lines[0])
        print(oxy_result)
    current_index += 1

print(int(c02_result, 2) * int(oxy_result, 2))

