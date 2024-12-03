with open("input.txt") as input:
    data = input.read()

def mul(x, y):
    sum = x * y
    return sum

sums = []
if "mul($,$)" in data:
    mul($, $)
    sum_to_be_appended = sum
    sums.append(sum_to_be_appended)

counter = 0
for i in sums:
    counter += i

print(counter)