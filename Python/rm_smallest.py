def rm_smallest(d):
    try:
        c = dict(d)
        del c[min(d, key=d.get)]
        return c
    except ValueError:
        return d


def test():
    assert 'a' in rm_smallest({'a': 1, 'b': -10}).keys()
    assert not 'b' in rm_smallest({'a': 1, 'b': -10}).keys()
    assert not 'a' in rm_smallest({'a': 1, 'b': 5, 'c': 3}).keys()
    rm_smallest({})
    print("Success!")


if __name__ == "__main__":
    test()
