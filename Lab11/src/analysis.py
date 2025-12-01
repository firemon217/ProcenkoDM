import matplotlib.pyplot as plt
from prefix_function import prefix_function
from z_function import z_function, z_search
from kmp_search import kmp_search
import time
from string_matching import rabin_karp, boyer_moore

def visualize_prefix_function(s: str):
    pi = prefix_function(s)
    plt.figure(figsize=(10, 4))
    plt.plot(range(len(s)), pi, marker='o')
    plt.title(f"Префикс-функция для '{s}'")
    plt.xlabel("Индекс")
    plt.ylabel("pi[i]")
    plt.grid(True)
    plt.show()

def visualize_z_function(s: str):
    z = z_function(s)
    plt.figure(figsize=(10, 4))
    plt.plot(range(len(s)), z, marker='o')
    plt.title(f"Z-функция для '{s}'")
    plt.xlabel("Индекс")
    plt.ylabel("z[i]")
    plt.grid(True)
    plt.show()

def measure_time(func, text, pattern):
    start = time.time()
    func(text, pattern)
    return time.time() - start

text_lengths = [1000, 5000, 10000, 50000, 100000]
pattern = "abcabc"
times_kmp = []
times_z = []
times_rk = []
times_bm = []

print("Начало эксперимента по сравнению алгоритмов поиска подстроки\n")
for n in text_lengths:
    text = "abc" * (n // 3)
    t_kmp = measure_time(kmp_search, text, pattern)
    t_z = measure_time(z_search, text, pattern)
    t_rk = measure_time(rabin_karp, text, pattern)
    t_bm = measure_time(boyer_moore, text, pattern)

    times_kmp.append(t_kmp)
    times_z.append(t_z)
    times_rk.append(t_rk)
    times_bm.append(t_bm)

    print(f"Длина текста: {n}")
    print(f"  KMP: {t_kmp:.6f} с")
    print(f"  Z-function: {t_z:.6f} с")
    print(f"  Rabin-Karp: {t_rk:.6f} с")
    print(f"  Boyer-Moore: {t_bm:.6f} с\n")

print("Сводка по алгоритмам:")
print(f"Среднее время KMP: {sum(times_kmp)/len(times_kmp):.6f} с")
print(f"Среднее время Z-function: {sum(times_z)/len(times_z):.6f} с")
print(f"Среднее время Rabin-Karp: {sum(times_rk)/len(times_rk):.6f} с")
print(f"Среднее время Boyer-Moore: {sum(times_bm)/len(times_bm):.6f} с\n")

# Построение графика
plt.plot(text_lengths, times_kmp, label="KMP", marker='o')
plt.plot(text_lengths, times_z, label="Z-function", marker='o')
plt.plot(text_lengths, times_rk, label="Rabin-Karp", marker='o')
plt.plot(text_lengths, times_bm, label="Boyer-Moore", marker='o')
plt.xlabel("Длина текста")
plt.ylabel("Время выполнения (с)")
plt.title("Сравнение алгоритмов поиска подстроки")
plt.legend()
plt.grid(True)
plt.show()

if __name__ == "__main__":
    sample_string = "ababcababcabc"
    print(f"Визуализация префикс-функции для строки: {sample_string}")
    visualize_prefix_function(sample_string)
    print(f"Визуализация Z-функции для строки: {sample_string}")
    visualize_z_function(sample_string)
