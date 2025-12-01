from typing import List, Dict

def rabin_karp(text: str, pattern: str, prime: int = 101) -> List[int]:
    """
    Алгоритм Рабина-Карпа для поиска подстроки.
    Временная сложность: O(n + m) в среднем, O(n*m) в худшем
    Пространственная сложность: O(1)
    """
    if not pattern:
        return []

    n, m = len(text), len(pattern)
    base = 256
    hpattern = 0
    htext = 0
    h = 1
    result = []

    for i in range(m - 1):
        h = (h * base) % prime

    for i in range(m):
        hpattern = (base * hpattern + ord(pattern[i])) % prime
        htext = (base * htext + ord(text[i])) % prime

    for i in range(n - m + 1):
        if hpattern == htext and text[i:i+m] == pattern:
            result.append(i)
        if i < n - m:
            htext = (base * (htext - ord(text[i]) * h) + ord(text[i + m])) % prime
            if htext < 0:
                htext += prime
    return result

def bad_character_table(pattern: str) -> Dict[str, int]:
    """
    Таблица плохого символа.
    """
    table = {}
    m = len(pattern)
    for i in range(m):
        table[pattern[i]] = i
    return table

def boyer_moore(text: str, pattern: str) -> List[int]:
    """
    Алгоритм Бойера-Мура для поиска подстроки.
    Временная сложность: O(n*m) в худшем, часто O(n/m) в среднем
    Пространственная сложность: O(m)
    """
    if not pattern:
        return []

    m = len(pattern)
    n = len(text)
    result = []
    bad_char = bad_character_table(pattern)
    s = 0

    while s <= n - m:
        j = m - 1
        while j >= 0 and pattern[j] == text[s + j]:
            j -= 1
        if j < 0:
            result.append(s)
            s += (m - bad_char.get(text[s + m], -1)) if s + m < n else 1
        else:
            s += max(1, j - bad_char.get(text[s + j], -1))
    return result
