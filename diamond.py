n=5
for i in range(-5 + 1, n):
        spaces = abs(i)
        stars = 2 * (n - spaces) - 1
        print(" " * spaces, end="")
        print("*" * stars)