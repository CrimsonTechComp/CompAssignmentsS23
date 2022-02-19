def rm_smallest(d):
    # Your code here!
    if d == {}:
        return {}
    x=min(d, key=d.get)
    print(x)
    del d[x]
    # for i in d:
    #    if d[i] == x: 
    #        del d[i]
    print(d)
    return d
    

def test():
    assert 'a' in rm_smallest({'a':1,'b':-10}).keys()
    assert not 'b' in rm_smallest({'a':1,'b':-10}).keys()
    assert not 'a' in rm_smallest({'a':1,'b':5,'c':3}).keys()
    rm_smallest({})
    print("Success!")

if __name__ == "__main__":
    test()
