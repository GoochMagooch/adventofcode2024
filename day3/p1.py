import re
with open("input.txt") as input:
    data = input.read()

def mul(x, y):
    sum = x * y
    return sum

# Use re.finditer to locate all occurrences of "mul(x,y)" and extract the arguments
pattern = r"mul\((\d+),(\d+)\)" # Matches mul(x,y) where x and y are integers
matches = re.finditer(pattern, data)

# Process each match
products = []
for match in matches:
    x, y = int(match.group(1)), int(match.group(2))  # Extract and convert arguments to integers
    products.append(mul(x, y))

counter = 0
for i in products:
    counter += i
print(counter)