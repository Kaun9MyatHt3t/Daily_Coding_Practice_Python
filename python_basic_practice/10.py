# Implement a recursive function to flatten a nested list of integers ( eg: [1,[2,[3,4]], 5] -> [1,2,3,4,5])
def get_flatten_list(data):
    result = []

    for item in data:
        if isinstance(item, int):
            result.append(item)
        elif isinstance(item, list):
            result.extend(get_flatten_list(item))
        else:
            raise TypeError("Only integers are allowed")
    return result

def main():
    print(get_flatten_list([1,[2,[3,4]], 5]))


if __name__ == "__main__":
    main()