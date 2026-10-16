
"""Program 28: Find common elements in two lists."""


def set_intersection(list1, list2):
    return sorted(set(list1) & set(list2))


if __name__ == "__main__":
    first = list(map(int, input("Enter first list: ").split()))
    second = list(map(int, input("Enter second list: ").split()))
    print("Common elements:", set_intersection(first, second))
