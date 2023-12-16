# Determine which games would have been possible if the bag had been loaded with only
# 12 red cubes, 13 green cubes, and 14 blue cubes.
# What is the sum of the IDs of those games?

possibles = {"red": 12, "green": 13, "blue": 14}


def process_gameline(gameline, possibles):
    """
    Game 1: 3 blue, 2 green, 6 red; 17 green, 4 red, 8 blue; 2 red, 1 green, 10 blue; 1 blue, 5 green
    """
    game, triesline = gameline.split(":")
    gamestr, gameno = game.strip().split(" ")
    print(f"{game} -> {triesline.strip()}")

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
            if int(amount) > possibles[color]:
                return 0

    # if we get here, return the game number
    return int(gameno.strip())


INPUT_FILE = "input.txt"

with open(INPUT_FILE) as file:
    sum_ids = 0
    for n, line in enumerate(file, start=1):
        gameline = line.strip()
        sum_ids = sum_ids + process_gameline(gameline, possibles)

print(f"The sum of the IDs is: {sum_ids}")
