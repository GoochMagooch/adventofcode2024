with open("input.txt") as input:
    data = input.read()

data_lines = data.split('\n')
new_data = []
for line in data_lines:
    lines = []
    lines.append(line)
    new_data.append(lines)

print(new_data.index("^"))