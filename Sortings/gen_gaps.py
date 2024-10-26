from math import *


def shell_gaps(n):  # N=25000 Time ~ 6.7
    a = []
    while (n > 1):
        n //= 2
        a.append(n)
    return a


def fib_gaps(n):
    if (n <= 2):
        return [1]
    l = [1, 1]
    for i in range(2, n):
        l.append(l[i - 2] + l[i - 1])
    return l[::-1][:-1]


def knut_gaps(n):
    a = []
    summ = 0
    k = 1
    while (summ < n / 3):
        summ = floor((3 ** k - 1) / 2)
        a.append(summ)
        k += 1
    return a[::-1]


def templay_gaps(n):
    def is_prime(num):
        if num < 2:
            return False
        for x in range(2, int(sqrt(num)) + 1):
            if num % x == 0:
                return False
        return True

    count = 2
    gaps = [1]

    while count <= n:
        if is_prime(count):
            gaps.append(count)
            count *= (1.5 * exp((count - 1) // count))
            count = int(count)
        else:
            count += 1

    return gaps[::-1]



if __name__ == "__main__":
    print(templay_gaps(10000))
