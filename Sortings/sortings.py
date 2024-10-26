import sys

sys.setrecursionlimit(100000)

# Inserstion Sort (Сортировка вставками)
def insertion_sort(a: list) -> list:
    '''
    Сортировка вставками
    '''
    n = len(a)
    for i in range(1, n):
        j = i - 1
        key = a[i]

        while j >= 0 and a[j] > key:
            a[j + 1] = a[j]
            j -= 1

        a[j + 1] = key
    return a


# Shell Sort (Сортировка шелла)
def shell_sort_shell(a: list):
    n = gap = len(a)

    while(gap>1):
        gap = gap // 2
        for i in range(gap, n, gap):
            j = i - gap
            key = a[i]
            while (j >= 0 and a[j] > key):
                a[j + gap] = a[j]
                j -= gap
            a[j + gap] = key
    return a

def shell_sort_hib(a: list):
    n = len(a)
    gap = 1
    while gap < n:
        gap = 2 * gap + 1
    while gap > 0:
        for i in range(gap, n, gap):
            j = i - gap
            key = a[i]
            while (j >= 0 and a[j] > key):
                a[j + gap] = a[j]
                j -= gap
            a[j + gap] = key
        gap = (gap - 1) // 2
    return a

def generate_pratt_gaps(n):
    gaps = []
    i = 0
    while True:
        gap = 2 ** i
        if gap > n:
            break
        j = 0
        while True:
            pratt_gap = gap * (3 ** j)
            if pratt_gap > n:
                break
            gaps.append(pratt_gap)
            j += 1
        i += 1
    gaps.sort(reverse=True)
    return gaps


def shell_sort_pratt(a: list):
    n = len(a)
    gaps = generate_pratt_gaps(n)

    for gap in gaps:
        for i in range(gap, n, gap):
            j = i - gap
            key = a[i]
            while j >= 0 and a[j] > key:
                a[j + gap] = a[j]
                j -= gap
            a[j + gap] = key
    return a



# Selection Sort (Сортировка выбором)
def selection_sort(a: list) -> list:
    '''
    Сортировка выбором
    '''
    n = len(a)
    for i in range(0, n - 1):
        max_elem = a[0]
        max_index = 0

        for j in range(1, n - i):
            if max_elem < a[j]:
                max_elem = a[j]
                max_index = j

        a[max_index], a[n - i - 1] = a[n - 1 - i], a[max_index]

    return a


# Merge Sort (Сортировка слиянием)
def merge(a, b):
    p1 = p2 = i = 0
    new_l = []
    n_len = len(a) + len(b)
    while p1 < len(a) and p2 < len(b):
        if a[p1] <= b[p2]:
            new_l.append(a[p1])
            p1 += 1
        else:
            new_l.append(b[p2])
            p2 += 1

    new_l.extend(a[p1:])
    new_l.extend(b[p2:])

    return new_l


def merge_sort(a: list) -> list:
    n = len(a)
    if n == 1:
        return a
    else:
        return merge(merge_sort(a[0: n // 2]), merge_sort(a[n // 2:n]))


# Bubble Sort (Сортировка пузырьком)
def bubble_sort(a):
    n = len(a)
    for i in range(0, n - 1):
        flag = False
        for j in range(0, n - i - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                flag = True
        if not flag:
            break
    return a



# Quick Sort (Быстрая сортировка)
def partition(a: list, p: int) -> (list, int):
    a[p], a[-1] = a[-1], a[p]
    key = a[-1]
    n = len(a)

    wall = 0
    for i in range(n - 1):
        if a[i] < key:
            a[wall], a[i] = a[i], a[wall]
            wall += 1
    a[-1], a[wall] = a[wall], a[-1]
    p = wall
    return a, p

    return a, p

def quick_sort(a: list) -> list:
    n = len(a)
    if n <= 1:
        return a

    pivot = 0
    a, pivot = partition(a, pivot)

    return quick_sort(a[0:pivot]) + [a[pivot]] + quick_sort(a[pivot + 1:n])


# Heap sort (Пирамидальная сортировка)

def swap(a: list, i, j):
    a[i], a[j] = a[j], a[i]


def heapify(a: list, n, i):
    l = i * 2 + 1
    r = i * 2 + 2
    largest = i

    if l < n and a[largest] < a[l]:
        largest = l

    if r < n and a[largest] < a[r]:
        largest = r

    if largest != i:
        swap(a, largest, i)

        heapify(a, n, largest)



def heap_sort(a: list) -> list:
    n = len(a)
    if (n <= 1):
        return a

    for i in range((n - 1) // 2, -1, -1):
        heapify(a, n, i)

    for i in range(n - 1, 0, -1):
        swap(a, 0, i)
        heapify(a, i, 0)


    return a


if __name__ == "__main__":
    a = [9, 16, 5, -5, 4, 4, 25, 12, 10, 18, 40]
    b = shell_sort_pratt(a.copy())
    if b == sorted(a):
        print("Ok")
    else:
        print("Not ok")