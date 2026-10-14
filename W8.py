def print_all(a):
    i = 0
    while i < len(a):
        print(a[i])
        i = i + 1


def print_2Dn(m):
    i = 0
    while i < len(m):
        j = 0
        while j < len(m[i]):
            print(m[i][j], end=" ")
            j = j + 1
        print()
        i = i + 1


def sum_2Dn(m):
    total = 0
    i = 0
    while i < len(m):
        j = 0
        while j < len(m[i]):
            total = total + m[i][j]
            j = j + 1
        i = i + 1
    return total


def count_2Dn(m, x):
    count = 0
    i = 0
    while i < len(m):
        j = 0
        while j < len(m[i]):
            if m[i][j] == x:
                count = count + 1
            j = j + 1
        i = i + 1
    return count


def addm(A, B):
    result = []
    i = 0
    while i < len(A):
        row = []
        j = 0
        while j < len(A[i]):
            row.append(A[i][j] + B[i][j])
            j = j + 1
        result.append(row)
        i = i + 1
    return result

m = [[5, 7, 9], [2, 4, 6], [8, 3, 1]]

print("2D list m:")
print_2Dn(m)

print("\nSum of all elements:", sum_2Dn(m))

x = 2
print("Count of", x, ":", count_2Dn(m, x))


A = [[1, 2], [3, 4]]
B = [[5, 6], [7, 8]]

print("\nMatrix A:")
print_2Dn(A)

print("\nMatrix B:")
print_2Dn(B)

C = addm(A, B)
print("\nA + B:")
print_2Dn(C)


with open("output.txt", "w") as file:
    file.write("2D list m:\n")
    i = 0
    while i < len(m):
        j = 0
        while j < len(m[i]):
            file.write(str(m[i][j]))
            if j < len(m[i]) - 1:
                file.write(" ")
            j = j + 1
        file.write("\n")
        i = i + 1

    file.write("Sum of all elements: " + str(sum_2Dn(m)) + "\n")
    file.write("Count of " + str(x) + ": " + str(count_2Dn(m, x)) + "\n")
    file.write("A + B:\n")

    i = 0
    while i < len(C):
        j = 0
        while j < len(C[i]):
            file.write(str(C[i][j]))
            if j < len(C[i]) - 1:
                file.write(" ")
            j = j + 1
        file.write("\n")
        i = i + 1

print("\nResults saved to output.txt")
