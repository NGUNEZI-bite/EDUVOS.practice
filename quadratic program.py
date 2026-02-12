import cmath
def solve_quadratic(A, B, C):
    if A ==0:
        print("Error: A cannot be zero.")
        return
    discriminant = B**2 -4*A*C

    if discriminant > 0:
        root1 = (-B + cmath.sqrt(discriminant)) / (2 * A)
        root2 = (-B - cmath.sqrt(discriminant)) / (2 * A)
        print("Roots are real and different: {root1.real}, {root2.real}")
    elif discriminant == 0:
            root = -B / (2 * A)
            print("the root is real and repeated: {root}")
    else:
        root1 = ( -B + cmath.sqrt(discriminant)) / (2 * A)
        root2 = ( -B - cmath.sqrt(discriminant)) / (2 * A)
        print(f" The roots are complex: {root1}, {root2}")



solve_quadratic(1, -3, 2)
