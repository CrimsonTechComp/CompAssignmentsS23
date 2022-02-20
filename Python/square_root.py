import math

def square_root(n):
    # Your code here!
    if isinstance(n, str) or n < 0:
        return -1
    else:
        x = n ** 0.5
    return x

def test():
    assert square_root(4) == 2
    assert square_root(0) == 0
    assert square_root("hello") == -1
    assert square_root(-10) == -1
    print("Success!")

if __name__ == "__main__":
    test()
