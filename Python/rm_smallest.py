def rm_smallest(d):
    # Your code here!
    if len(d) == 0:
        return d
    min_value = min(d.values())
    s = dict()
    
    for i,j in d.items():
        if j !=min_value:
            s[i]=j
    return s

def test():
    assert 'a' in rm_smallest({'a':1,'b':-10}).keys()
    assert not 'b' in rm_smallest({'a':1,'b':-10}).keys()
    assert not 'a' in rm_smallest({'a':1,'b':5,'c':3}).keys()
    rm_smallest({})
    print("Success!")

if __name__ == "__main__":
    test()
