numbers = []

try:
    with open("example.txt", "r") as file:
        for line in file:
            num = int(line)
            numbers.append(num)

    if len(numbers) > 0:
        max_value = numbers[0]
        min_value = numbers[0]
        total = 0
        i = 0

        while i < len(numbers):
            if numbers[i] > max_value:
                max_value = numbers[i]

            if numbers[i] < min_value:
                min_value = numbers[i]

            total = total + numbers[i]
            i = i + 1

        average = total / len(numbers)

        print("Numbers:")
        for num in numbers:
            print(num)

        print("Maximum:", max_value)
        print("Minimum:", min_value)
        print("Average:", average)

        with open("output.txt", "w") as file:
            file.write("Numbers:\n")

            for num in numbers:
                file.write(str(num) + "\n")

            file.write("Maximum: " + str(max_value) + "\n")
            file.write("Minimum: " + str(min_value) + "\n")
            file.write("Average: " + str(average) + "\n")

        print("Results saved to output.txt")

    else:
        print("The file contains no numbers.")

except FileNotFoundError:
    print("Error: example.txt is not found")