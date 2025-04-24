def generate_pyramid(n, char='*'):
    if not isinstance(n, int) or n < 1 or n > 20:
        raise ValueError("n must be an integer between 1 and 20.")
    if char not in ('*', '#'):
        raise ValueError("char must be either '*' or '#'.")

    lines = []
    for i in range(n):
        num_chars = 2 * i + 1
        line = char * num_chars
        lines.append(line.center(2 * n - 1))
    return '\n'.join(lines)

if __name__ == "__main__":
    while True:
        try:
            n = int(input("Enter the number of pyramid levels (1-20): "))
            if not (1 <= n <= 20):
                print("Invalid input: Please enter a number between 1 and 20.")
                continue

            char = input("Enter the pyramid character (* or #): ").strip()
            if char not in ('*', '#'):
                print("Invalid character: Only '*' or '#' are allowed.")
                continue

            print("Generated Pyramid:\n")
            print(generate_pyramid(n, char))
            break

        except ValueError:
            print("Invalid input. Please enter valid values.")
