# Write a function that takes two sets and returns a tuple with three sets : interaction, union and symmetric difference.
def get_analyzed(s1 : set[int], s2 : set[int])-> tuple[set, set, set]:
    union = s1 & s2
    intersect = s1 | s2
    difference = s1 ^ s2
    return union, intersect, difference


def main():
    s1 = {1,2,3,4,5}
    s2 = {2,4,5,6,8}

    result = get_analyzed(s1, s2)
    print(result)


if __name__ == "__main__":
    main()