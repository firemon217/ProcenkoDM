import time
import tracemalloc
from dynamic_programming import fib_memo, fib_iter, knapsack


def measure(func, *args):
    """Измеряем время и потребление памяти функцией func."""
    tracemalloc.start()
    start = time.perf_counter()

    result = func(*args)

    elapsed = time.perf_counter() - start
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    return result, elapsed, peak


def compare_fibonacci(n=35):
    print("=== Сравнение Top-Down (мемоизация) и Bottom-Up ===")
    print(f"n = {n}")

    res_memo, time_memo, mem_memo = measure(fib_memo, n)
    res_iter, time_iter, mem_iter = measure(fib_iter, n)

    print("\nTop-Down (мемоизация):")
    print(f"  Значение:        {res_memo}")
    print(f"  Время:           {time_memo:.6f} сек")
    print(f"  Память (пик):    {mem_memo / 1024:.2f} КБ")

    print("\nBottom-Up (итеративный):")
    print(f"  Значение:        {res_iter}")
    print(f"  Время:           {time_iter:.6f} сек")
    print(f"  Память (пик):    {mem_iter / 1024:.2f} КБ")

    print("\nВывод:")
    print("  Bottom-Up обычно быстрее и использует меньше памяти.")
    print("  Top-Down удобнее в реализации, но вызывает накладные расходы.")

def fractional_knapsack(weights, values, capacity):
    """Реализует жадный алгоритм для непрерывного рюкзака."""
    items = list(zip(weights, values))
    # сортировка по убыванию value/weight
    items.sort(key=lambda x: x[1] / x[0], reverse=True)

    total_value = 0
    remaining = capacity

    for w, v in items:
        if w <= remaining:
            # берём весь предмет
            total_value += v
            remaining -= w
        else:
            # берём дробь предмета
            total_value += v * (remaining / w)
            break

    return total_value


def compare_knapsack():
    print("\n=== Сравнение жадного fractional и ДП для 0-1 knapsack ===")

    weights = [10, 20, 30]
    values = [60, 100, 120]
    capacity = 50

    dp_result = knapsack(weights, values, capacity)
    greedy_result = fractional_knapsack(weights, values, capacity)

    print(f"\nВес: {weights}")
    print(f"Ценность: {values}")
    print(f"Вместимость: {capacity}")

    print("\nЖадный fractional knapsack:")
    print(f"  Результат: {greedy_result}")

    print("\nДП для 0-1 knapsack:")
    print(f"  Результат: {dp_result}")

    print("\nВывод:")
    print("  Жадный алгоритм работает ТОЛЬКО для непрерывного рюкзака.")
    print("  Для 0-1 рюкзака он может дать НЕ оптимальное решение.")
    print("  Динамическое программирование всегда гарантирует оптимальный результат.")

if __name__ == "__main__":
    compare_fibonacci(35)
    compare_knapsack()

