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
colors_all = ["green", "brown", "orange", "red", "yellow", "aqua", "steelblue", "olive", "red"]


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


def plot_graph(name, case_index, is_regession=False, clr=None, printname=False):
    """
    Рисует график для какого либо случая.
    :param name: имя сортировки
    :param case_index: индекс нужного нам случая
    :param is_regession: делать ли регрессию?
    :param color: Цвет графика и регрессионной кривой
    :return:
    """

    lbl = cases_dict[case_index]
    if printname:
        lbl = name

    pt = json_work.Json_Saver(name)

    case = pt.get_case(cases_dict[case_index])  # Получаем нужный нам случай

    # Получаем значения x = n и y = t
    x = np.array(list(map(int, case.keys())))
    y = np.array(list(map(float, case.values())))

    # Строим график


    plt.plot(x, y, 'o', label=lbl, color=clr)

    if is_regession:
        # ОПРЕДЕЛЯЕМ ТИП ФУНКЦИИ РЕГРЕССИИ В ЗАВИСИМОСТИ ОТ СЛУЧАЯ СОРТИРОВКИ
        if name in ("bubble_sort", "insertion_sort", "selection_sort"):
            test_func = quadratic
            if name == "bubble_sort" and case_index == 0:
                test_func = linear
        elif name in ("merge_sort", "heap_sort", "quick_sort"):
            test_func = nlogn
            if name == "quick_sort" and cases_dict[case_index] != "Average Case":
                test_func = quadratic
        elif "shell" in name:
            test_func = quadratic
            if name == "shell_sort_shell":
                if case_index == 0: test_func = nlogn
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

        print(f"{test_func.__name__} Для {cases_dict[case_index]} случая: a={param[0]}, b={param[1]}, c={param[2]}")

        arg = test_func(x, param[0], param[1], param[2])


        plt.plot(x, arg, "-", label=f"Регрессия для {lbl}", color=clr)

        plt.legend()
        plt.tight_layout()











    # MAIN CODE
# Выбор метода сортировки
print("Запущен main.py")
print("Выберите метод/методы сторитровки: ")
for key, value in names.items():
    print(f"[{key}] {value}")
numbers = [int(i) for i in input("Номер(а): ").split()]
if len(numbers) == 1:
    n = numbers[0]
for i in numbers:
    print(names[i])



print(cases_dict)
cases = [int(i) for i in input("Какой нужен случай (через пробел): ").split()]
print(cases)

# is_on_one_graph = int(input("Выводить ли случаи на один график? 0 - Нет. 1 - Да"))

is_do_regression = int(input("Делать ли регрессию? 0 - Нет. 1 - Да"))




# Отрисовка графика для каждой сортировки.
for sort_index in numbers:
    print(f"Рисуем график для {names[sort_index]}")

    plt.xlabel('Количество элементов массива')
    plt.ylabel('Время в секундах')

    plt.title(names[sort_index])


    if len(cases) == 1:
        plot_graph(names[sort_index], cases[0], is_do_regression, colors_all[sort_index], True)

    else:
        for case_index in cases:
            plot_graph(names[sort_index], case_index, is_do_regression, cases_color[case_index])

        # Сохранение графика в файл.
        regr = "_regr" if is_do_regression else ""
        plt.savefig(f"Results/{names[sort_index]}{regr}.png")
        plt.show()

    print(f"График для {names[sort_index]} успешно отрисован\n")

if len(cases) == 1:
    # Сохранение графика в файл.
    plt.title("Сравнение сортировок")

    plt.savefig(f"Results/Many_Sortings.png")
    plt.show()

print("Графики успешно отрисованы. Конец программы.")