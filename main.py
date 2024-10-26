# Matplotlib for graphics
import matplotlib.pyplot as plt
import matplotlib

# Numpy for regression
import numpy as np
from scipy.optimize import curve_fit

import json_work
# Sorting testing function
import sorting_testing as st

names = {0: 'bubble_sort', 1: 'heap_sort', 2: 'insertion_sort', 3: 'merge_sort', 4: 'quick_sort', 5: 'selection_sort',
 6: 'shell_sort_hib', 7: 'shell_sort_pratt', 8: 'shell_sort_shell'}

cases_dict = {0: "Sorted", 1: "Partially Sorted", 2: "Worst Case", 3: "Average Case"}

def quadratic(X, a, b, c):
    return a * np.power(X, 2) + b * X + c


def nlogn(X, a, b, c):
    return a * np.log(X) + b * X + c


def linear(X, k, b):
    return k * X + b

def plot_graph(name, cases, is_regession=False):
    pt = json_work.Json_Saver(names[n])

    for case_index in cases:
        case = pt.get_case(cases_dict[case_index]) # Получаем нужный нам случай

        x = np.array(list(map(int, case.keys())))
        y = np.array(list(map(float, case.values())))

        plt.plot(x, y, 'o', label=cases_dict[case_index])

        if is_regession:
            # ОПРЕДЕЛЯЕМ ТИП СОРТИРОВКИ
            if name in ("bubble_sort", "insertion_sort", "selection_sort"):
            param, _ = curve_fit(quadratic, x, y)



    plt.xlabel('Количество элементов массива')
    plt.ylabel('Теоретическое время в секундах')
    plt.title(name)

    plt.legend()
    plt.grid(True)
    plt.show()


# MAIN CODE
# Выбор метода сортировки
print("Запущен main.py")
print("Выберите метод сторитровки: ")
for key, value in names.items():
    print(f"[{key}] {value}")
n = int(input("Номер: "))
print(names[n])

print(cases_dict)
cases = [int(i) for i in input("Какой нужен случай (через пробел): ").split()]
plot_graph(names[n], cases)

assert 0 == 1

new_pr = st.Json_Saver(names[n])
param, param_cov = 0



if n in (0, 5, 6):
    case_sorted = new_pr.get_case(st.cases_dict[0])
    case_partially = new_pr.get_case(st.cases_dict[1])
    case_worst = new_pr.get_case(st.cases_dict[2])
    case_average = new_pr.get_case(st.cases_dict[3])

    x = numpy.array(list(map(int, data2.keys())))
    y = numpy.array(list(map(float, data2.values())))

    param, _ = curve_fit(quadratic, x, y)

print(case_sorted, case_partially, case_worst, case_average, sep='\n')

matplotlib.rcParams.update({'font.size': 12})

plt.plot(case_sorted.keys(), case_sorted.values(), 'go', label='Sorted')
plt.plot(case_partially.keys(), case_partially.values(), 'bo', label='Partially')
plt.plot(case_average.keys(), case_average.values(), 'yo', label='Average')
plt.plot(case_worst.keys(), case_worst.values(), 'ro', label='Worst')

plt.legend(fontsize=12)

plt.tight_layout()

plt.show()
