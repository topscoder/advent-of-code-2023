import re

INPUT_FILE = "example.part2.1.txt"

matrix = []
sum = 0


def get_all_numbers(line):
    return re.findall("\d{1,}", line.strip())


def get_all_gears(line):
    return re.findall("[\*]{1}", line.strip())


with open(INPUT_FILE) as file:
    for n, line in enumerate(file, start=1):
        n = n - 1
        matrix.append(list(line.strip()))

    for n, elems in enumerate(matrix):
        if n == 0:
            continue

        line = "".join(matrix[n])

        gears = get_all_gears(line)

        START_SEARCH = 0
        for gear in gears:
            PREV_LINE = "".join(matrix[n - 1])
            CUR_LINE = "".join(matrix[n])
            NEXT_LINE = "".join(matrix[n + 1]) if n + 1 < len(matrix) else ""

            GEAR_POSITION = CUR_LINE.find("*", START_SEARCH)
            search_start = 0 if GEAR_POSITION == 0 else GEAR_POSITION - 1
            search_end = search_start + 2

            # get all numbers of previous line
            # and check if any of these numbers is adjacent to the gear
            # by checking it's existence within search_start and search_end
            print("")
            print(f"{n-1}:> {PREV_LINE}")
            print(f"{n}:{GEAR_POSITION} {line}")
            print(f"{n+1}:> {NEXT_LINE}")

            # get numbers in previous line
            # to find out if any of these numbers is adjacent
            # to our current gear (of loop)
            # prev_line_numbers = re.findall("\d{1,}", PREV_LINE.strip())
            prev_line_numbers = get_all_numbers(PREV_LINE)
            prev_line_num_start_search = 0
            for number in prev_line_numbers:
                prev_line_num_start = PREV_LINE.find(number, prev_line_num_start_search)
                prev_line_num_end = prev_line_num_start + len(number) - 1
                print(
                    f"number {number} has position {prev_line_num_start},{prev_line_num_end}"
                )
                if GEAR_POSITION >= (prev_line_num_start - 1) and GEAR_POSITION <= (
                    prev_line_num_end + 1
                ):
                    print(
                        f"{number} of prev line is adjacent to the gear {GEAR_POSITION} ({prev_line_num_start-1},{prev_line_num_end+1})"
                    )

                    # FIXME it's possible the next number in the current line (prev line) is the next adjacent
                    # to this same exact gear

                    # get numbers in next line
                    # to find out if any of these numbers is adjacent
                    # to our current gear (of loop)
                    next_line_numbers = get_all_numbers(NEXT_LINE)
                    next_line_num_start_search = 0
                    for next_line_number in next_line_numbers:
                        next_line_num_start = NEXT_LINE.find(
                            next_line_number, next_line_num_start_search
                        )
                        next_line_num_end = next_line_num_start + len(number) - 1
                        if GEAR_POSITION >= (
                            next_line_num_start - 1
                        ) and GEAR_POSITION <= (next_line_num_end + 1):
                            print(
                                f"{next_line_number} of next line is adjacent to the gear {GEAR_POSITION} ({next_line_num_start-1},{next_line_num_end+1})"
                            )
                            print(f">>> {number}x{next_line_number}")
                            sum = sum + (int(number) * int(next_line_number))
                            break

                        next_line_num_start_search = next_line_num_end

                    prev_line_num_start_search = prev_line_num_end

            # move the start search pointer
            # so the current gear wont be matched in next loop
            START_SEARCH = GEAR_POSITION

    print(f"The sum of all of the gear ratios in your engine schematic: {sum}")
