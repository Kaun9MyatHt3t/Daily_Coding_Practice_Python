# Write a function that takes a list of integers and returns a dictionary with keys "even" and "odd" containing lists of even and odd numbers respectively
# list of integer input, output dict with even and odd and list of numbers
from typing import List, Dict


def get_dict(data : List[int]) -> Dict[str, List[int]]:
    # return {"even":[x for x in data if x % 2 == 0], "odd": [x for x in data if x % 2 == 1]} <- slower , but pythonic.
    result = {"even": [], "odd": []}
    for x in data:
        if x %2 == 0:
            result["even"].append(x)
        else:
            result["odd"].append(x)
    return result # <- Better Efficiency


def main():
    sample_list = list(map(int, input("> ").split()))
    result = get_dict(sample_list)
    print(result)

if __name__ == "__main__":
    main()
