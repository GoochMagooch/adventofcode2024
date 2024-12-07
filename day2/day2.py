with open('input.txt') as levels:
    data = levels.read()

data_list = []
for line in data:
    new_data = data.replace('\n', ',')
    data_final = new_data.split(',')

for item in data_final:
    data_list.append(item)

data_int_strings = []
for item in data_list:
    data_int_strings.append(item.split(' '))

data_ints = []
for item in data_int_strings:
    ints_list = []
    for i in item:
        ints_list.append(int(i))
    data_ints.append(ints_list)
print(data_ints)