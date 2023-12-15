
# find first digit
def first_num(input_str):
    index = 0

    while True:
        # See if the part from the pointer position to the end of the string contains a spelled digit
        spelled = [
            "one",
            "two",
            "three",
            "four",
            "five",
            "six",
            "seven",
            "eight",
            "nine",
        ]

        for i, spelled_char in enumerate(spelled):
            if spelled_char in input_str[0:index]:
                return int(i) + 1

        # See if the character at pointer position is a literal numeric
        char = input_str[index]
        if char in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            return char

        index = index + 1


# find last digit
def last_num(input_str):
    pointer = len(input_str)
    index = 1

    while True:
        # See if the character at pointer position is a literal numeric
        char = input_str[pointer - index]
        if char in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            return char

        # See if the part from the pointer position to the end of the string contains a spelled digit
        spelled = [
            "one",
            "two",
            "three",
            "four",
            "five",
            "six",
            "seven",
            "eight",
            "nine",
        ]

        for i, spelled_char in enumerate(spelled):
            if spelled_char in input_str[pointer - index :]:
                return int(i) + 1

        index = index + 1


INPUT_FILE = "input.txt"
sum = 0

with open(INPUT_FILE) as file:
    for n, line in enumerate(file, start=1):
        line = line.strip()

        first = first_num(line)
        last = last_num(line)

        print(f"{line} -> {first}:{last}")

        sum = sum + int(f"{first}{last}")

print(f"The sum of this puzzle is: {sum}")
