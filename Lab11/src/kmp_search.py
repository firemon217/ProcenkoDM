from prefix_function import prefix_function
from typing import List

def kmp_search(text: str, pattern: str) -> List[int]:
    """
    Поиск всех вхождений pattern в text с использованием алгоритма KMP.
    
    Временная сложность: O(n + m)
    Пространственная сложность: O(m)
    """
    if not pattern:
        return []

    combined = pattern + "#" + text
    pi = prefix_function(combined)
    result = []
    m = len(pattern)
    for i in range(m + 1, len(combined)):
        if pi[i] == m:
            result.append(i - 2 * m)
    return result
