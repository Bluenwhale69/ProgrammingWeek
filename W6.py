def sum_1_to_n(n):
    sum_val = 0
    count = 1
    while count <= n:
        sum_val += count
        count += 1
    return sum_val


def find_max(a):
    max_val = a[0]
    i = 1
    while i < len(a):
        if max_val < a[i]:
            max_val = a[i]
        i += 1
    return max_val


def is_sorted(a):
    i = 0
    while i < len(a) - 1:
        if a[i] > a[i + 1]:
            return False
        i += 1
    return True


def main():
    print("Sum 1 to 5:", sum_1_to_n(5))

    a = [5, 9, 2]
    print("Max:", find_max(a))
    print("Is sorted?:", is_sorted(a))

    s = "Hello"
    print("ASCII of 'a':", ord('a'))
    print("Char of 97:", chr(97))
    print("Upper:", s.upper())


if __name__ == "__main__":
    main()