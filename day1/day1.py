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

# appending the differences of a[n] and b[n] to a list 'diffs'
diffs = []
counter = 0
for i in range(len(a)):
    if a[counter] > b[counter]:
        diffs.append(a[counter] - b[counter])
    elif a[counter] < b[counter]:
        diffs.append(b[counter] - a[counter])
    counter += 1

# finds the sum of all differences from 'diffs'
counter = 0
for i in diffs:
    counter += i
# desired output: 2264607
print(counter)