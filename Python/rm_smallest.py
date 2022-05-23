def rm_smallest(d):
  things = d.items()
  min_val = min(d.values())
  for (k, v) in things: 
    if v == min_val:
      del d[k]
      break
    else:
      continue
  return 0;


def test():
    assert 'a' in rm_smallest({'a':1,'b':-10}).keys()
    assert not 'b' in rm_smallest({'a':1,'b':-10}).keys()
    assert not 'a' in rm_smallest({'a':1,'b':5,'c':3}).keys()
    rm_smallest({})
    print("Success!")

if __name__ == "__main__":
    test()
