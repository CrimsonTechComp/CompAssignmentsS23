def sum(lst, n):
    # initialize the sum to zero
    total = 0
    
    # loop over the list and add each element to the total
    for num in lst:
        total += num
    
    # check if the sum equals the given number n and return the appropriate boolean value
    return total == n

def test():
    assert sum([-1, 1], 0)
    assert not sum([0,2,3], 4)
    assert sum([0,2,2], 4)
    print("Success!")

if __name__ == "__main__":
    test()
