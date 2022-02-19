def rm_smallest(d):
    values = d.values()
    if len(values) == 0:
        return d
    values_list = list(values)
    minimum = min(values_list)
    return {key:val for key, val in d.items() if val != minimum}

def test():
    assert 'a' in rm_smallest({'a':1,'b':-10}).keys()
    assert not 'b' in rm_smallest({'a':1,'b':-10}).keys()
    assert not 'a' in rm_smallest({'a':1,'b':5,'c':3}).keys()
    rm_smallest({})
    print("Success!")

if __name__ == "__main__":
    test()
