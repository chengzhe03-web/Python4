def add(a: float, b: float) -> float:
    return a + b


def subtract(a: float, b: float) -> float:
    return a - b


def main() -> None:
    print("Simple Calculator")
    print("1) Add")
    print("2) Subtract")

    choice = input("Choose (1/2): ").strip()

    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))

    if choice == "1":
        print("Result:", add(a, b))
    elif choice == "2":
        print("Result:", subtract(a, b))
    else:
        print("Invalid choice")


if __name__ == "__main__":
    main()
