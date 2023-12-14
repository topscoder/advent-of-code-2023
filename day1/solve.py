import re

# find first digit
def first_num(input_str):
    match = re.search(r'\d', input_str)
    return int(match.group())

# find last digit
def last_num(input_str):
    matches = re.findall(r'\d', input_str)
    return int(matches[-1])

input_file = "input.txt"
sum = 0

with open(input_file) as file:
    for n, line in enumerate(file, start=1):
        first = first_num(line.strip())
        last = last_num(line.strip())
        sum = sum + int(f"{first}{last}")

print(f"The sum of this puzzle is: {sum}")