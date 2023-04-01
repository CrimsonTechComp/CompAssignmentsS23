import random


def random_ints():
    ls = []
    r = 0
    while r != 6:
        r = random.randint(1, 10)
        ls.append(r)
    return ls


def test():
    N = 10000
    total_length = 0
    for i in range(N):
        l = random_ints()
        assert not 0 in l
        assert not 11 in l
        assert l[-1] == 6
        total_length += len(l)
    assert abs(total_length / N - 10) < 1  # checks that the length of the random lists are reasonable.
    print("Success!")


if __name__ == "__main__":
    test()
