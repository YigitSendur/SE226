def task1():
    num = int(input("Enter a positive integer greater than 9: "))

    steps = 0
    print(num, end="")

    while num >= 10:
        temp = num
        digit_sum = 0

        # basamakları toplama
        while temp > 0:
            digit_sum += temp % 10
            temp //= 10

        print(" →", digit_sum, end="")
        num = digit_sum
        steps += 1

    print("Final value:", num)
    print("Total steps:", steps)

def task2():
    n=int(input("Please enter a number which between 10 and 100 "))
    while n<10 or n>100:
        n=int(input("Invalid number . Please enter a between 10 and 100 "))

    fizz=0
    buzz=0
    fizzbuzz=0

    for i in range(1, n + 1):

        if i % 7 == 0:
            continue

        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
            fizzbuzz += 1
        elif i % 3 == 0:
            print("Fizz")
            fizz += 1
        elif i % 5 == 0:
            print("Buzz")
            buzz += 1
        else:
            print(i)

    print("--- Summary ---")
    print(f"Fizz count   : {fizz}")
    print(f"Buzz count   : {buzz}")
    print(f"FizzBuzz count: {fizzbuzz}")

def task3():
    n=int(input("please enter an number between 3-9"))
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print(j, end=" ")
        print()

    for i in range(n-1, 0, -1):
        for j in range(1, i + 1):
            print(j, end=" ")
        print()


if __name__ == "__main__":
    task1()
    task2()
    task3()

