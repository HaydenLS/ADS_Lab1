import random
import time
import math
import Sortings.sortings as s
from json_work import *

cases_dict = {0: "Sorted", 1: "Partially Sorted", 2: "Worst Case", 3: "Average Case"}


def get_random_array(n: int, left: int, right=None, seed=None):
    if right is None:
        right = left
        left = -left
    if seed is not None:
        random.seed = seed

    return [random.randint(left, right) for _ in range(n)]


def partially_sorted(arr: list):
    """
    :param arr: Массив
    :return: **новый** частично отсортированный массив (90/10)
    """
    n = len(arr)
    els_sorted = math.floor(n * 0.9)

    return sorted(arr[:els_sorted + 1]) + arr[els_sorted + 1:]


def sorted_reverse(arr: list):
    """
    :param arr: Массив
    :return: **новый** отсортированный в обратном порядке массив (90/10)
    """
    return sorted(arr, reverse=True)


def test_sort_base(srt_method, length_array: list, check_in_times=5, method_gen_arrays=None):
    """
    :param srt_method: Метод сортировки
    :param length_array: Список размеров
    :param check_in_times: Колиество проверок для одного размера массива
    :param method_gen_arrays: Метод генерации массивов
    :return:
    """
    a = list()
    for n in length_array:

        times = list()
        for i in range(check_in_times):
            # Generation of random array

            array = get_random_array(n, 0, 10000)  # изменить границы по возможности
            if method_gen_arrays is not None:
                array = method_gen_arrays(array)
            print(f"Происходит сортировка для метода {srt_method.__name__}. Случай: {method_gen_arrays}")
            # Getting time of sort
            begin = time.time()
            result = srt_method(array)
            end = time.time()
            t = end - begin

            times.append(t)
        # Рассчитываем среднее время
        sr_time = sum(times) / len(times)

        a.append((n, sr_time))

    return a


if __name__ == "__main__":
    # Выбор метода сортировки
    print("Запущен sorting_testing.py")
    print("Выберите метод сторитровки: ")
    names = [i for i in dir(s) if "sort" in i]
    for i in range(len(names)):
        print(f"[{i}] {names[i]}")
    n = int(input("Номер: "))
    print(names[n])

    # ДАЛЬШЕ ИДУТ ТЕСТЫ СОРИТРОВОК (7 СОРТИРОВОК)

    print(cases_dict)
    case_n = [int(i) for i in input("Какой нужен случай (через пробел): ").split()]

    n_quadratic = [i for i in range(1000, 10001, 1000)]
    n_log_n = [i for i in range(50000, 500001, 25000)]

    checkin_times = 3
    # ЗАДАЕМ МАССИВ С КОЛИЧЕСТВОМ ЭЛЕМЕНТОВ
    if names[n] in ("bubble_sort", "insertion_sort", "selection_sort"):
        list_of_elements_n = n_quadratic

    if names[n] in ("quick_sort", "merge_sort", "heap_sort"):
        list_of_elements_n = n_log_n

    if names[n] == "shell_sort_shell":
        list_of_elements_n = [i for i in range(1000, 15001, 1000)]

    if names[n] == "shell_sort_hib":
        list_of_elements_n = [i for i in range(1000, 15001, 1000)]

    if names[n] == "shell_sort_pratt":
        list_of_elements_n = [i for i in range(1000, 15001, 1000)]

    name = names[n]  # Имя функции
    f_name = getattr(s, name)  # Ссылка на саму функцию

    pr = Json_Saver(name)

    method_gen = None
    for tip in case_n:
        match tip:
            case 0:
                method_gen = sorted
            case 1:
                method_gen = partially_sorted
            case 2:
                method_gen = sorted_reverse
            case 3:
                method_gen = None
        if(name == "quick_sort"):
            if cases_dict[tip] != "Average Case":
                list_of_elements_n = n_quadratic
        result = test_sort_base(f_name, list_of_elements_n, 3, method_gen)
        pr.add_case(result, cases_dict[tip])
        print(f"Для сортировки {name} добавлен случай {cases_dict[tip]}")

    print("Метод отработан успешно")
