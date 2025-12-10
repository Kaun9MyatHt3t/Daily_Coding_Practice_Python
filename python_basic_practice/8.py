# Write a function that takes a list of integers and returns a new list with elements doubled if they are odd, tripled if even.
from typing import List


def get_new_list(data : List[int]) -> List[int]:
    return [x * 3 if x % 2 == 0 else x * 2 for x in data]


def main():
    sample = list(map(int, input(">").split()))
    result = get_new_list(sample)
    print(result)


if __name__ == "__main__":
    main()