def sum(lst, n):
    count = 0 
    for x in lst:
        count += x
    return count == n 

def test():
    assert sum([-1, 1], 0)
    assert not sum([0,2,3], 4)
    assert sum([0,2,2], 4)
    print("Success!")

if __name__ == "__main__":
    test()
