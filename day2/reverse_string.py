def reverse_string(string):
    original = list(string)
    new = ""
    for i in range(len(original) - 1, -1, -1):
        new += original[i]
    return new


if __name__ == "__main__":
    string = input("Enter a string to reverse: ")
    print(reverse_string(string))
