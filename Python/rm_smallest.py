# take in argument d
def rm_smallest(d):
    # if the dictionary is empty, return the original dictionary
    if not d:
        return d

    # find the minimum value in the dictionary
    min_value = min(d.values())

    # find the key(s) that correspond to the minimum value
    min_keys = [k for k, v in d.items() if v == min_value]

    # remove the key-value pair(s) from the dictionary
    for k in min_keys:
        d.pop(k)

    # return the modified dictionary
    return d

def test():
    assert 'a' in rm_smallest({'a':1,'b':-10}).keys()
    assert not 'b' in rm_smallest({'a':1,'b':-10}).keys()
    assert not 'a' in rm_smallest({'a':1,'b':5,'c':3}).keys()
    assert rm_smallest({}) == {}
    print("Success!")

if __name__ == "__main__":
    test()
