def print_results(a, b, max_value):
    for x in range(max_value + 1):
        result = a * 2 * x + b
        print(f"{a} x 2 x {x} + {b} = {result}")


def main():
    a = int(input("a: "))
    b = int(input("b: "))
    max_value = int(input("max: "))

    print_results(a, b, max_value)


if __name__ == "__main__":
    main()