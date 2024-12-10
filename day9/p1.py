with open("input.txt") as input:
    data = input.read()

ids = []
counter = 0
digit = 0
for i in data:
    id = []
    if counter % 2 == 0:
        id.append(str(i) + " data block, " + "ID: " + str(digit))
        counter += 1
        ids.append(id)
        id = []
        digit += 1
    else:
        counter += 1
        continue
print(ids)