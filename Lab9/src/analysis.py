import time
import matplotlib.pyplot as plt
from dynamic_programming import knapsack


def knapsack_visual(weights, values, capacity):
    n = len(weights)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        w = weights[i - 1]
        v = values[i - 1]

        for cap in range(1, capacity + 1):
            if w > cap:
                dp[i][cap] = dp[i - 1][cap]
            else:
                dp[i][cap] = max(dp[i - 1][cap], dp[i - 1][cap - w] + v)

    # Вывод таблицы после заполнения
    print("DP-таблица (каждая строка — предмет, каждая колонка — вместимость):")
    for row in dp:
        print(row)

    return dp[n][capacity]

def knapsack_scalability_test():
    import random

    print("\n=== Экспериментальное исследование масштабируемости 0-1 рюкзака ===")
    
    # Параметры эксперимента
    item_counts = [5, 10, 20, 30, 40, 50]  # количество предметов
    capacity = 50
    times = []

    for n in item_counts:
        weights = [random.randint(1, 10) for _ in range(n)]
        values = [random.randint(10, 100) for _ in range(n)]

        start = time.perf_counter()
        knapsack(weights, values, capacity)
        elapsed = time.perf_counter() - start

        print(f"n = {n}, время = {elapsed:.6f} сек")
        times.append(elapsed)

    # Построение графика зависимости времени от числа предметов
    plt.figure(figsize=(8,5))
    plt.plot(item_counts, times, marker='o')
    plt.title("Зависимость времени работы DP рюкзака от числа предметов")
    plt.xlabel("Количество предметов")
    plt.ylabel("Время выполнения (сек)")
    plt.grid(True)
    plt.show()

if __name__ == "__main__":

    # Визуализация DP-таблицы для маленького примера
    weights = [10, 20, 30]
    values = [60, 100, 120]
    capacity = 50

    print("=== Визуализация DP-таблицы ===")
    result = knapsack_visual(weights, values, capacity)
    print(f"Максимальная ценность: {result}")

    # Исследование масштабируемости
    knapsack_scalability_test()
