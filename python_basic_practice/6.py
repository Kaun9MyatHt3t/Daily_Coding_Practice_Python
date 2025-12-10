# Merge two dictionaries , if a key exists in both, sum their values
from collections import Counter


def main():
    d1 = {"a":2, "b":6}
    d2 = {"a":3, "c":4}

    result =  Counter(d1) + Counter(d2)
    print(sorted(result.items(), key=lambda x: x[0]))


if __name__ == "__main__":
    main()