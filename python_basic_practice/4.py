# using a dictionary comprehension , create a dictionary mapping numbers 1-20 to their squares, but only include numbers divisible by 3.
from random import sample
from typing import List, Dict


def get_dict() -> Dict[int, int]:
    return {key: key**2 for key in range(1, 21) if key%3 == 0}


def main():
    result = get_dict()
    print(result)


if __name__ == "__main__":
    main()