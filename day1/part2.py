with open('input.txt') as num_in:
    num_input = num_in.read()

# converts text file to list of elements that each contain 2 large numbers
for line in num_input:
    input_replaced = num_input.replace('   ', ' ')
    input_replaced_two = input_replaced.replace('\n', ',')
    std_input = input_replaced_two.split(',')

input_list = []
for item in std_input:
    input_list.append(item.split(' '))

# converting all strings in 0th and 1st index of input_list to ints and sorting
a_strings = []
for item in input_list:
    a_strings.append(int(item[0]))
a = sorted(a_strings)

b_strings = []
for item in input_list:
    b_strings.append(int(item[1]))
b = sorted(b_strings)

# iterates throught list a and counts the number of times it is in list b
# then multiplies i by the number of times it is repeated in list b
product_counter = 0
for i in a:
    product = 0
    counter = 0
    for j in b:
        if i == j:
            counter += 1
    product = i * counter
    product_counter += product

# desired output: 19457120
print(product_counter)