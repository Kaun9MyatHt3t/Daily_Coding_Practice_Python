# write a function that takes a tuple (a, b, *rest) and returns a*b plus the sum of all elements in rest.
from typing import List


def get_result(a : int, b : int, *args : int)->int:
    return a*b + sum(args)


def main():
    a, b, *rest = list(map(int, input(">").split()))
    result = get_result(a, b, *rest)
    print(result)


if __name__ == "__main__":
    main()


