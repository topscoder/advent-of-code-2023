# As you continue your walk, the Elf poses a second question:
# in each game you played, what is the fewest number of cubes
# of each color that could have been in the bag to make the game possible?
# For each game, find the minimum set of cubes that must have been present.
# What is the sum of the power of these sets?


def process_gameline(gameline):
    """
    Game 1: 3 blue, 2 green, 6 red; 17 green, 4 red, 8 blue; 2 red, 1 green, 10 blue; 1 blue, 5 green
    """
    game, triesline = gameline.split(":")
    gamestr, gameno = game.strip().split(" ")
    print(f"{game} -> {triesline.strip()}")
    max_cubes_per_try = {"red": 0, "green": 0, "blue": 0}

    game_tries = triesline.strip().split(";")

    # foreach try check if try is within boundaries of possibles:
    # gameline is valid if all tries fit within boundaries
    for game_try in game_tries:
        reveals = game_try.strip().split(",")
        for reveal in reveals:
            reveal = reveal.strip()
            amount, color = reveal.split(" ")
            print(f"reveal: {amount} x {color}")

            # if the reveal doesn't fit in possibles, return 0
            if int(amount) > max_cubes_per_try[color]:
                max_cubes_per_try[color] = int(amount)

    # if we get here, return the game number
    print(max_cubes_per_try)

    return max_cubes_per_try["red"] * max_cubes_per_try["green"] * max_cubes_per_try["blue"]


INPUT_FILE = "input.txt"

with open(INPUT_FILE) as file:
    sum = 0
    for n, line in enumerate(file, start=1):
        gameline = line.strip()
        sum = sum + process_gameline(gameline)

print(f"The sum of the pows is: {sum}")
