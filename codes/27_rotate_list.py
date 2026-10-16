
"""Program 27: Rotate a list to the right."""


def rotate_list(numbers, k):
    if not numbers:
        return []

    k = k % len(numbers)

    if k == 0:
        return numbers.copy()

    return numbers[-k:] + numbers[:-k]


if __name__ == "__main__":
    numbers = list(map(
        int, input("Enter numbers separated by spaces: ").split()
    ))
    k = int(input("Enter rotation positions: "))
    print("Rotated list:", rotate_list(numbers, k))
