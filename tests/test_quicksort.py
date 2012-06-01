from random import randint

from sys import path
path.append('..')

from quicksort import quicksort

def test_quicksort():
    test_list = [randint(1, 50) for i in range(15)]
    test_sorted = test_list[:]
    quicksort(test_sorted, 0, 14)
    if test_sorted == sorted(test_list):
        print("test passes")
        print(test_list)
        print(test_sorted)
    else:
        print("test fails")
        print(test_list)
        print(test_sorted)

if __name__ == "__main__":
    test_quicksort()
