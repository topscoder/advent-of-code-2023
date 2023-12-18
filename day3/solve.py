"""
The engine schematic (your puzzle input) consists of a visual representation of the engine.
There are lots of numbers and symbols you don't really understand,
but apparently any number adjacent to a symbol, even diagonally,
is a "part number" and should be included in your sum.
(Periods (.) do not count as a symbol.)

What is the sum of all of the part numbers in the engine schematic?

"""
import re

INPUT_FILE = "input.txt"

matrix = []
sum = 0


with open(INPUT_FILE) as file:
    for n, line in enumerate(file, start=1):
        n = n - 1
        matrix.append(list(line.strip()))


for n, elems in enumerate(matrix):
    line = "".join(matrix[n])
    symbols = set(["@", "#", "$", "%", "&", "*", "-", "=", "+", "/"])
    numbers = re.findall("\d{1,}", line.strip())

    START_SEARCH = 0
    for number in numbers:
        PREV_LINE = "".join(matrix[n - 1])
        CUR_LINE = "".join(matrix[n])
        NEXT_LINE = "".join(matrix[n + 1]) if n + 1 < len(matrix) else ""

        # if current number exists more than once in current line,
        # We need to find the right position
        POS_START = CUR_LINE.find(number, START_SEARCH)
        POS_END = POS_START + len(number) - 1
        search_start = 0 if POS_START == 0 else POS_START - 1
        search_end = POS_END + 2

        # Next to symbol in actual line?
        print(f"")
        print(f"number {number} in line {n}")
        if any(char in symbols for char in CUR_LINE[search_start:search_end]):
            print(f"symbol found in current line: {CUR_LINE[search_start:search_end]}")
            sum = sum + int(number)

        # Next to a symbol in previous line?
        elif n > 0 and any(
            char in symbols for char in PREV_LINE[search_start:search_end]
        ):
            print(
                f"symbol found in previous line: {PREV_LINE[search_start:search_end]}"
            )
            sum = sum + int(number)

        # Next to a symbol in
        elif any(char in symbols for char in NEXT_LINE[search_start:search_end]):
            print(f"symbol found in next line: {NEXT_LINE[search_start:search_end]}")
            sum = sum + int(number)

        START_SEARCH = POS_START + 1

print(f"The sum of all of the part numbers in the engine schematic: {sum}")
