# Demonstrate the difference between deep copy and shallow copy by creating a list of lists, modifying a nested element and printing both copies to show the effect
import copy


def main():
    sample = [
        [1,2,3],
        [4,5,6]
    ]

    # deep copy
    d = copy.deepcopy(sample)

    # shallow copy
    s = sample.copy()

    sample[1][1] = 99
    print(d)
    print(s)

if __name__ == "__main__":
    main()