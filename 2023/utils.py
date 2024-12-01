import os


def load_data(test: bool = False):
    FILENAME = "puzzle.txt"
    if test:
        FILENAME = "sample_puzzle.txt"
    PUZZLE_DATA_PATH = os.path.join("./inputs", FILENAME)
    with open(PUZZLE_DATA_PATH) as f:
        puzzle_data = f.read().splitlines()
    return puzzle_data
