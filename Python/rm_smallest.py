def rm_smallest(d):
    if not d:
        return d
    # vals = list(d.values())
    
    # del d[next(iter(vals.index(max(vals))))]
    min_k = next(iter(d))
    min_v = d[min_k]
    for key, val in d.items():
        if min_v > val:
            min_v = val
            min_k = key
    d.pop(min_k)
    return d

def test():
    assert 'a' in rm_smallest({'a':1,'b':-10}).keys()
    assert not 'b' in rm_smallest({'a':1,'b':-10}).keys()
    assert not 'a' in rm_smallest({'a':1,'b':5,'c':3}).keys()
    rm_smallest({})
    print("Success!")

if __name__ == "__main__":
    test()
