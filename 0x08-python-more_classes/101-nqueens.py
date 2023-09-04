#!/usr/bin/python3
""" Defines nqueens program and print the coordinates of n queens"""


from sys import argv

if __name__ == "__main__":
    a = []
    if len(argv) != 2:
        print("Usage: nqueens N")
        exit(1)
    if argv[1].isdigit() is False:
        print("N must be a number")
        exit(1)
    n = int(argv[1])
    if n < 4:
        print("N must be at least 4")
        exit(1)

    # initialize the answer list
    for t in range(n):
        a.append([t, None])

    def already_exists(y):
        """check queen availability on othjer values"""
        for x in range(n):
            if y == a[x][1]:
                return True
        return False

    def reject(x, y):
        """determines the solution"""
        if (already_exists(y)):
            return False
        t = 0
        while(t < x):
            if abs(a[t][1] - y) == abs(t - x):
                return False
            t += 1
        return True

    def clear_a(x):
        """ to clear answers from point of failure """
        for t in range(x, n):
            a[t][1] = None

    def nqueens(x):
        """recursive function to find the solution"""
        for y in range(n):
            clear_a(x)
            if reject(x, y):
                a[x][1] = y
                if (x == n - 1):  # equal to solution
                    print(a)
                else:
                    nqueens(x + 1)  # increment x value to next

    nqueens(0)
