with open("input.txt") as input:
    data = input.read()

ids = []
counter = 0
digit = 0
for i in data:
    if counter % 2 == 0:
        ids.append(digit)
        counter += 1
        digit += 1
    else:
        counter += 1
        continue

free_space = []
count = 0
for i in data:
    if count % 2 == 1:
        free_space.append(i)
        count += 1
    else:
        count += 1
        continue

# alterning through both above lists and adding to `id_free_space`
id_free_space = []
for i in range(len(ids)):
    id_free_space.append(ids[i])
    id_free_space.append(int(free_space[i]))

print(id_free_space)