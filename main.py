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
cases_color = {0: "green", 1: "darkorange", 2: "red", 3: "blue"}


def quadratic(X, a, b, c):
    return a * np.power(X, 2) + b * X + c


def poltora(X, a, b, c):
    return a * np.power(X, 1.5) + b * X + c


def odin_dvadcat_pyat(X, a, b, c):
    return a * np.power(X, 1.25) + b * X + c


def nlogn_quadrat(X, a, b, c):
    return a * np.log(X) ** 2 + b * X + c


def nlogn(X, a, b, c):
    return a * np.log(X) + b * X + c


def linear(X, k, b, c):
    return k * X + b


def plot_graph(name, cases, is_regession=False):
    pt = json_work.Json_Saver(names[n])

    for case_index in cases:
        case = pt.get_case(cases_dict[case_index])  # Получаем нужный нам случай

        # Получаем значения x = n и y = t
        x = np.array(list(map(int, case.keys())))
        y = np.array(list(map(float, case.values())))

        # Строим график
        clr = cases_color[case_index]
        plt.plot(x, y, 'o', label=cases_dict[case_index], color=clr)

        if is_regession:
            # ОПРЕДЕЛЯЕМ ТИП ФУНКЦИИ РЕГРЕССИИ В ЗАВИСИМОСТИ ОТ СЛУЧАЯ СОРТИРОВКИ
            if name in ("bubble_sort", "insertion_sort", "selection_sort"):
                test_func = quadratic
                if name == "bubble_sort" and case_index==0:
                    test_func = linear
            elif name in ("merge_sort", "heap_sort", "quick_sort"):
                test_func = nlogn
                if name == "quick_sort" and cases_dict[case_index] != "Average Case":
                    test_func = quadratic
            elif "shell" in name:
                test_func = quadratic
                if name == "shell_sort_shell":
                    if case_index == 2: test_func = nlogn
                    if case_index == 3: test_func = poltora
                if name == "shell_sort_hib":
                    if case_index in (0, 1): test_func = nlogn
                    if case_index == 3: test_func = odin_dvadcat_pyat
                    if case_index == 2: test_func = poltora
                if name == "shell_sort_pratt":
                    if case_index in (0, 1): test_func = nlogn
                    if case_index in (2, 3): test_func = nlogn_quadrat

            param, _ = curve_fit(test_func, x, y)
            # print(f"Регрессия для метода {name} в случае будет описываться функцией {test_func.__name__}")

            print(f"Для {cases_dict[case_index]} случая: a={param[0]}, b={param[1]}, c={param[2]}")

            arg = test_func(x, param[0], param[1], param[2])

            plt.plot(x, arg, "-", label=f"Регрессия для {cases_dict[case_index]}", color=clr)

    plt.xlabel('Количество элементов массива')
    plt.ylabel('Время в секундах')
    plt.title(name)

    plt.legend()
    plt.grid(True)


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
print(cases)

is_do_regression = int(input("Делать ли регрессию? 0 - Нет. 1 - Да"))

plot_graph(names[n], cases, is_do_regression)

regr = "_regr" if is_do_regression else ""
plt.savefig(f"Results/{names[n]}{regr}.png")

plt.show()

