from typing import List

def prefix_function(s: str) -> List[int]:
    """
    Вычисляет префикс-функцию для строки s.
    pi[i] = длина наибольшего собственного префикса, который совпадает с суффиксом, заканчивающимся в позиции i.
    
    Временная сложность: O(n)
    Пространственная сложность: O(n)
    """
    n = len(s)
    pi = [0] * n
    for i in range(1, n):
        j = pi[i - 1]
        while j > 0 and s[i] != s[j]:
            j = pi[j - 1]
        if s[i] == s[j]:
            j += 1
        pi[i] = j
    return pi
