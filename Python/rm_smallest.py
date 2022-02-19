import sys 

def rm_smallest(d):
    # Your code here!
    if d == {}:
        return d 
    
    smallest = sys.maxsize 
    small_key = sys.maxsize 

    for key in d: 
        if d[key] < smallest:
            smallest = d[key]
            small_key = key 
    del d[small_key] 
    
    return d 

def test():
    assert 'a' in rm_smallest({'a':1,'b':-10}).keys()
    assert not 'b' in rm_smallest({'a':1,'b':-10}).keys()
    assert not 'a' in rm_smallest({'a':1,'b':5,'c':3}).keys()
    rm_smallest({})
    print("Success!")

if __name__ == "__main__":
    test()
