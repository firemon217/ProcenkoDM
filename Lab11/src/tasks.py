from prefix_function import prefix_function
from kmp_search import kmp_search


def find_all_occurrences(text: str, pattern: str):
    """
    Возвращает список индексов всех вхождений pattern в text.
    Используется алгоритм KMP.
    """
    return kmp_search(text, pattern)

def find_period(s: str):
    """
    Ищет минимальный период строки s.
    Период t строки s означает, что s = t^k для некоторого k.
    Использует префикс-функцию.
    """
    n = len(s)
    if n == 0:
        return 0  # пустая строка не имеет периода
    pi = prefix_function(s)
    period = n - pi[-1]
    if n % period == 0:
        return period
    else:
        return n  # период отсутствует, период = длина строки

def is_cyclic_shift(s1: str, s2: str):
    """
    Проверяет, можно ли получить s2 циклическим сдвигом s1.
    """
    if len(s1) != len(s2):
        return False
    return s2 in (s1 + s1)

if __name__ == "__main__":
    text = "abcabcabc"
    pattern = "abc"
    print("Все вхождения паттерна:", find_all_occurrences(text, pattern))

    s = "ababab"
    print(f"Период строки '{s}':", find_period(s))

    s1 = "abcde"
    s2 = "deabc"
    print(f"'{s2}' является циклическим сдвигом '{s1}'?", is_cyclic_shift(s1, s2))
