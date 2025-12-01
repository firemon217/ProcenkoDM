from typing import List

def z_function(s: str) -> List[int]:
    """
    Вычисляет Z-функцию для строки s.
    Z[i] = длина наибольшего префикса строки, совпадающего с подстрокой, начинающейся в позиции i.
    
    Временная сложность: O(n)
    Пространственная сложность: O(n)
    """
    n = len(s)
    z = [0] * n
    l = r = 0
    for i in range(1, n):
        if i <= r:
            z[i] = min(r - i + 1, z[i - l])
        while i + z[i] < n and s[z[i]] == s[i + z[i]]:
            z[i] += 1
        if i + z[i] - 1 > r:
            l, r = i, i + z[i] - 1
    return z

def z_search(text: str, pattern: str) -> List[int]:
    """
    Поиск всех вхождений pattern в text с использованием Z-функции.
    """
    if not pattern:
        return []

    combined = pattern + "#" + text
    z = z_function(combined)
    m = len(pattern)
    result = []
    for i in range(m + 1, len(combined)):
        if z[i] == m:
            result.append(i - m - 1)
    return result
