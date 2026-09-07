from solver import solve_quadratic

def get_coefficient(name: str) -> float:
    """Prompt the user for a valid floating-point coefficient."""
    while True:
        try:
            return float(input(f"Enter coefficient {name}: "))
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def main():
    print("=" * 40)
    print("   Quadratic Equation Solver (ax² + bx + c = 0)")
    print("=" * 40)

    while True:
        a = get_coefficient("a")
        if a == 0:
            print("Coefficient 'a' cannot be 0 for a quadratic equation. Try again.")
            continue
        break

    b = get_coefficient("b")
    c = get_coefficient("c")

    try:
        r1, r2 = solve_quadratic(a, b, c)
        print("\n--- Results ---")
        if r1 == r2:
            print(f"One real root: x = {r1}")
        else:
            print(f"Root 1: x1 = {r1}")
            print(f"Root 2: x2 = {r2}")
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()

