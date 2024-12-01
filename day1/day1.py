with open('input.txt') as num_in:
    num_input = num_in.read()


num_lines_list = []
for line in num_input:
    num_lines_replaced = num_input.replace('   ', ' ')
    num_lines_replaced_two = num_lines_replaced.replace('\n', ',')
    std_input = num_lines_replaced_two.split(',')

std_input_list = []
for item in std_input:
    std_input_list.append(item.split(' '))

# converting all items in 0th and 1st index of std_input_list to list of separate strings of numbers
std_input_a_strings = []
for item in std_input_list:
    std_input_a_strings.append(list(item[0]))

std_input_b_strings = []
for item in std_input_list:
    std_input_b_strings.append(list(item[1]))


# converts all sublists of strings of numbers to ints
std_a = []
for item in std_input_a_strings:
    std_a_ints = []
    for i in item:
        std_a_ints.append(int(i))
    std_a.append(std_a_ints)

std_b = []
for item in std_input_b_strings:
    std_b_ints = []
    for i in item:
        std_b_ints.append(int(i))
    std_b.append(std_b_ints)

# sorts both lists of ints
std_a_sorted = []
for item in std_a:
    std_a_sorted.append(sorted(item))

std_b_sorted = []
for item in std_b:
    std_b_sorted.append(sorted(item))

# converts all sorted sublists into a single list
ints_sep_a = []
for item in std_a_sorted:
    for i in item:
        ints_sep_a.append(i)

ints_sep_b = []
for item in std_b_sorted:
    for i in item:
        ints_sep_b.append(i)

