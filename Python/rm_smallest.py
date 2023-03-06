def rm_smallest(d):
    if not d:
        return d 
    else:
        min_value = min(d.values())
        min_key = [k for k, v in d.items() if v == min_value][0]
        d.pop(min_key)
        return d 
    

def test():
    assert 'a' in rm_smallest({'a':1,'b':-10}).keys()
    assert not 'b' in rm_smallest({'a':1,'b':-10}).keys()
    assert not 'a' in rm_smallest({'a':1,'b':5,'c':3}).keys()
    rm_smallest({})
    print("Success!")

if __name__ == "__main__":
    test()
