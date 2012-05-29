from random import randint

from sys import path
path.append('..')

from insertion_sort import insertion_sort

def test_insertion_sort():
    test_list = [randint(1, 50) for i in range(15)]
    test_sorted = insertion_sort(test_list[:])
    if test_sorted == sorted(test_list):
        print("test passes")
        print(test_list)
        print(test_sorted)
    else:
        print("test fails")
        print(test_list)
        print(test_sorted)

if __name__ == "__main__":
    test_insertion_sort()
