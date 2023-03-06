import math
from numbers import Number

def square_root(n):
    # Your code here!
    if (not isinstance(n, Number) or n < 0):
        return -1
    else:
        return n**0.5

def test():
    assert square_root(4) == 2
    assert square_root(0) == 0
    assert square_root("hello") == -1
    assert square_root(-10) == -1
    print("Success!")

if __name__ == "__main__":
    test()
