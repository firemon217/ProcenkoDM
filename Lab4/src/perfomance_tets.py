from generate_data import generate_datasets
from sorts import *
import timeit
import sys
import plot_result 

sys.setrecursionlimit(10000) 

SIZES = [100, 1000, 5000]

SORTS = {
    "Bubble": bubble_sort,
    "Selection": selection_sort,
    "Insertion": insertion_sort,
    "Merge": merge_sort,
    "Quick": quick_sort
}

def measure_time(sort_fn, arr, runs=5):
    statement = "sort_fn(test_arr.copy())"
    setup = (
        "from __main__ import sort_fn, test_arr"
    )

    global sort_fn_global, test_arr
    sort_fn_global = sort_fn
    test_arr = arr

    total_time = timeit.timeit(
        stmt="sort_fn_global(test_arr.copy())",
        number=runs,
        globals=globals()
    )

    return total_time / runs

if __name__ == "__main__":
    datasets = generate_datasets(SIZES)
    print("\n=== BENCHMARK START ===\n")
    for size, types in datasets.items():
        print(f"\n------------------------------")
        print(f"Размер массива: {size}")
        print(f"------------------------------\n")
        for data_type, arr in types.items():
            print(f"\nТип данных: {data_type}")
            for sort_name, sort_fn in SORTS.items():
                time_sec = measure_time(sort_fn, arr)
                plot_result.plot_creater(sort_name, size, time_sec, data_type)
    plot_result.plot_graph("random")  # график для случайных данных
    plot_result.plot_graph("sorted")  # график для отсортированных данных
    plot_result.plot_graph("reversed")  # график для обратного порядка
    plot_result.plot_graph("almost_sorted")  # почти отсортированные