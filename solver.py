import cmath
import math

def solve_quadratic(a: float, b: float, c: float):
    if a == 0:
        raise ValueError("Coefficient 'a' cannot be zero in a quadratic equation.")

    discriminant = (b ** 2) - (4 * a * c)

    if discriminant >= 0:
        root1 = (-b + math.sqrt(discriminant)) / (2 * a)
        root2 = (-b - math.sqrt(discriminant)) / (2 * a)
    else:
        root1 = (-b + cmath.sqrt(discriminant)) / (2 * a)
        root2 = (-b - cmath.sqrt(discriminant)) / (2 * a)

    return root1, root2
