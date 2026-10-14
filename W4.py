def sum(n):
    i = 1
    sum_val = 0

    while i <= n:
        sum_val += i
        i += 1

    print(f"ผลรวมจาก 1 ถึง {n} คือ: {sum_val}")


def loop_sum_until():
    sum_total = 0

    while True:
        num = int(input("กรอกตัวเลข : "))

        if num == -1:
            break

        sum_total += num
        print(f"ผลรวมสะสมทั้งหมด: {sum_total}")

    print(f"ผลรวมสะสมทั้งหมดสุดท้าย: {sum_total}")


def print_line(n):
    while n > 0:
        print("*", end="")
        n -= 1
    print()


sum(20)
loop_sum_until()
print_line(5)
