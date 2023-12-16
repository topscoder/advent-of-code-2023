"""
The engine schematic (your puzzle input) consists of a visual representation of the engine.
There are lots of numbers and symbols you don't really understand,
but apparently any number adjacent to a symbol, even diagonally,
is a "part number" and should be included in your sum.
(Periods (.) do not count as a symbol.)

What is the sum of all of the part numbers in the engine schematic?

"""
import re

INPUT_FILE = "example.txt"

matrix = []
sum = 0


with open(INPUT_FILE) as file:
    for n, line in enumerate(file, start=1):
        n = n - 1
        matrix.append(list(line.strip()))


for n, elems in enumerate(matrix):
    line = "".join(matrix[n])
    numbers = re.findall("\d{1,}", line.strip())
    symbols = set(["@", "#", "$", "%", "&", "*", "-", "=", "+", "/"])

    # if is_part_number(number, matrix):
    for number in numbers:
        CUR_LINE_WITHOUT_DOTS = line.strip().replace(".", "")

        cur_line_position_start = CUR_LINE_WITHOUT_DOTS.find(number)
        cur_line_position_end = cur_line_position_start + len(number) - 1
        cur_line_search_start = (
            0 if cur_line_position_start == 0 else cur_line_position_start - 1
        )
        cur_line_search_end = cur_line_position_end + 2

        PREV_LINE = "".join(matrix[n - 1])
        CUR_LINE = "".join(matrix[n])
        NEXT_LINE = "".join(matrix[n + 1]) if n + 1 < len(matrix) else ""

        position_start = CUR_LINE.find(number)
        position_end = position_start + len(number) - 1
        search_start = (
            0 if position_start == 0 else position_start - 1
        )
        search_end = position_end + 2

        # Next to symbol in actual line?
        print(f"")
        print(f"number {number} in line {n}")
        if any(
            char in symbols
            for char in CUR_LINE[cur_line_search_start:cur_line_search_end]
        ):
            print(
                f"symbol found in current line: {CUR_LINE[cur_line_search_start:cur_line_search_end]}"
            )
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

print(f"The sum of all of the part numbers in the engine schematic: {sum}")
