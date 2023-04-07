import math
# takes a single argument, n.
def square_root(n):
  if isinstance(n, (int, float)):
        if n >= 0:
            return math.sqrt(n)
  return -1


def test():
    assert square_root(4) == 2
    assert square_root(0) == 0
    assert square_root("hello") == -1
    assert square_root(-10) == -1
    print("Success!")

if __name__ == "__main__":
    test()
