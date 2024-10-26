# Re-import necessary libraries after state reset
import numpy as np
import matplotlib.pyplot as plt

n_values = np.linspace(100, 1000, 100)

merge_sort = 1.75 * n_values * np.log(n_values)
quick_sort = 0.5 * n_values * np.log(n_values)
heap_sort = 1.5 * n_values * np.log(n_values)
shell_sort_shell_gaps = n_values ** 1.5
shell_sort_hibbard_gaps = n_values ** 1.25
shell_sort_pratt_gaps = n_values * np.log(n_values) ** 2


plt.plot(n_values, merge_sort, label='Merge Sort', color='purple')
plt.plot(n_values, quick_sort, label='Quick Sort', color='orange')
plt.plot(n_values, heap_sort, label='Heap Sort', color='brown')
plt.plot(n_values, shell_sort_shell_gaps, label='Shell Sort (Shell Gaps)', color='red')
plt.plot(n_values, shell_sort_hibbard_gaps, label='Shell Sort (Hibbard Gaps)', color='blue')
plt.plot(n_values, shell_sort_pratt_gaps, label='Shell Sort (Pratt Gaps)', color='green')

plt.xlabel('Количество элементов')
plt.ylabel('Теоретическое время')

plt.legend()
plt.grid(True)
# plt.show()
plt.savefig('saved.png')

