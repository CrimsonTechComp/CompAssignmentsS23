import random

def random_ints():
# initialize an empty list to store the numbers
  numbers = []
  # initialize a variable to store the current number
  number = 0
  # loop until the number is 6
  while number != 6:
    # generate a random number in the range [1,10]
    number = int(random.random()*10) + 1
    # append the number to the list
    numbers.append(number)
  return numbers

def test():
    N = 10000
    total_length = 0
    for i in range(N):
        l = random_ints()
        assert not 0 in l
        assert not 11 in l
        assert l[-1] == 6
        total_length += len(l)
    assert abs(total_length / N - 10) < 1 # checks that the length of the random strings are reasonable.
    print("Success!")

if __name__ == "__main__":
    test()
