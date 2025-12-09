# Given a string, return a new string that contains every 3rd character in reverse order
def get_slice(data : str)-> str:
    return data[2::3][::-1]


def main():
    sample = "holaworld"
    print(get_slice(sample))


if __name__ == "__main__":
    main()

