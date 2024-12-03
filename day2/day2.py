with open('input.txt') as levels:
    data = levels.readlines()

for line in data:
    counter = 0
    for i in line:
        if i[counter] < i[counter + 1] & i[counter + 1] - i[counter] <= 3:
            print(i)