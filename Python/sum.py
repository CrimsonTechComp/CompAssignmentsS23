def sum(lst, n):
    total = 0
    for num in lst:
        total += num
    return (n == total)

def test():
    assert sum([-1, 1], 0)
    assert not sum([0,2,3], 4)
    assert sum([0,2,2], 4)
    print("Success!")

if __name__ == "__main__":
    test()
