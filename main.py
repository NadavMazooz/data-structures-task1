# pylint: disable=invalid-name,missing-module-docstring

import random
from result import Result

result = Result()


def search1(V: list[int], m: int, x: int) -> int:
    """Search function number 1 - O(n) """
    for i in range(m):
        result.search1_count += 1

        if V[i] == x:
            return i

        if V[i] == 0:
            return -1

    return -1


def search2(V: list[int], m: int, x: int) -> int:
    """Search function number 2 - O(logm) """

    high = m - 1
    low = 0
    mid = 0

    while low <= high:
        result.search2_count += 1

        mid = (high + low) // 2

        # If x is smaller or point to 0 area, ignore right half
        if V[mid] > x or V[mid] == 0:
            high = mid - 1

        # If x is greater, ignore left half
        elif V[mid] < x:
            low = mid + 1

        # means x is present at mid
        else:
            return mid

    # If we reach here, then the element was not present
    return -1


def search3(V: list[int], m: int, x: int) -> int:
    """Search function number 3 - O(logn) """
    n = find_n(V, m)  # O(log100) ~ O(1)

    high = n - 1
    low = 0
    mid = 0

    while low <= high:
        result.search3_count += 1

        mid = (high + low) // 2

        # If x is smaller or point to 0 area, ignore right half
        if V[mid] > x or V[mid] == 0:
            high = mid - 1

        # If x is greater, ignore left half
        elif V[mid] < x:
            low = mid + 1

        # means x is present at mid
        else:
            return mid

    # If we reach here, then the element was not present
    return -1


def find_n(V: list[int], m: int) -> int:
    '''Get list of integers, return max number in the list - O(log100)'''
    low = 200
    high = min(300, m-1)

    max_number = V[low]
    max_number_index = low

    while low <= high:
        mid = (high + low) // 2

        if V[mid] > max_number:
            max_number = V[mid]
            max_number_index = mid
            low = mid + 1

        elif V[mid] == 0:
            high = mid - 1

        else:
            return max_number_index

    return max_number_index


def initial_list(n: int, m: int) -> list[int]:
    '''Create initial list for test assertion'''
    l = []
    min_number = 1
    max_number = 1000000

    for i in range(n):
        number = random.randint(min_number, max_number)
        l.append(number)

    l = sorted(l)

    extra_zeros = m-n

    for i in range(extra_zeros):
        l.append(0)

    x = random.randint(min_number, max_number)
    return l, x


def main():
    """Main function"""
    number_of_iterations = 500

    for i in range(number_of_iterations):
        random_n = random.randint(200, 300)
        m = 1000
        V, x = initial_list(random_n, m)

        search1(V, m, x)
        search2(V, m, x)
        search3(V, m, x)

    print('200<=n<=300')
    print('search1: ', result.get_search1_average(number_of_iterations))
    print('search2: ', result.get_search2_average(number_of_iterations))
    print('search3: ', result.get_search3_average(number_of_iterations))


main()
