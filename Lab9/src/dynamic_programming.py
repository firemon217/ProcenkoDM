def fib_naive(n):
    # Базовые случаи: F(0)=0, F(1)=1
    if n <= 1:
        return n
    # Рекурсивное определение F(n)
    return fib_naive(n - 1) + fib_naive(n - 2)
# Время: O(2^n)
# Память: O(n) — глубина рекурсии

def fib_memo(n, memo=None):
    if memo is None:
        memo = {}

    if n <= 1:
        return n

    # Если значение уже вычислялось — вернуть из memo
    if n in memo:
        return memo[n]

    # Сохраняем результат, чтобы не вычислять повторно
    memo[n] = fib_memo(n - 1, memo) + fib_memo(n - 2, memo)
    return memo[n]
# Время: O(n)
# Память: O(n) для словаря memo + глубины рекурсии

def fib_iter(n):
    if n <= 1:
        return n

    # Создаём таблицу dp[0..n]
    dp = [0] * (n + 1)
    dp[1] = 1

    # Заполняем таблицу снизу вверх
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]

    return dp[n]
# Время: O(n)
# Память: O(n) (можно уменьшить до O(1))

def knapsack(weights, values, capacity):
    n = len(weights)

    # dp[i][w] — максимум ценности, если берем первые i предметов и рюкзак имеет вместимость w
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    # Заполняем таблицу
    for i in range(1, n + 1):
        w = weights[i - 1]  # вес текущего предмета
        v = values[i - 1]   # ценность текущего предмета

        for cap in range(1, capacity + 1):

            if w > cap:
                # Не можем взять предмет — просто копируем значение сверху
                dp[i][cap] = dp[i - 1][cap]
            else:
                # Максимум между игнорированием и включением предмета
                dp[i][cap] = max(
                    dp[i - 1][cap],            # не берем предмет
                    dp[i - 1][cap - w] + v     # берем предмет
                )

    return dp[n][capacity]
# Время: O(n * W)
# Память: O(n * W)

def lcs(a, b):
    n, m = len(a), len(b)

    # dp[i][j] — длина LCS для a[:i] и b[:j]
    dp = [[0] * (m + 1) for _ in range(n + 1)]

    # Заполняем таблицу
    for i in range(1, n + 1):
        for j in range(1, m + 1):

            if a[i - 1] == b[j - 1]:
                # Символы совпадают → увеличиваем LCS на 1
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                # Иначе берём максимум из верхнего и левого
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    return dp[n][m]
# Время: O(n * m)
# Память: O(n * m)


def levenshtein(a, b):
    n, m = len(a), len(b)

    # dp[i][j] — минимальная стоимость преобразования первых i символов a в первые j символов b
    dp = [[0] * (m + 1) for _ in range(n + 1)]

    # Если строка пустая — стоимость равна количеству вставок/удалений
    for i in range(n + 1):
        dp[i][0] = i
    for j in range(m + 1):
        dp[0][j] = j

    # Заполняем таблицу
    for i in range(1, n + 1):
        for j in range(1, m + 1):

            if a[i - 1] == b[j - 1]:
                # Если символы равны — стоимость не увеличивается
                dp[i][j] = dp[i - 1][j - 1]
            else:
                # Выбираем минимальную операцию: удаление, вставка или замена
                dp[i][j] = 1 + min(
                    dp[i - 1][j],    # удаление
                    dp[i][j - 1],    # вставка
                    dp[i - 1][j - 1] # замена
                )

    return dp[n][m]
# Время: O(n * m)
# Память: O(n * m)

def lcs_with_reconstruction(a, b):
    n, m = len(a), len(b)

    # Строим DP-таблицу
    dp = [[0] * (m + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if a[i - 1] == b[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    # Теперь восстанавливаем LCS
    i, j = n, m
    lcs_str = []

    while i > 0 and j > 0:
        # Если символы совпадают - добавляем в ответ
        if a[i - 1] == b[j - 1]:
            lcs_str.append(a[i - 1])
            i -= 1
            j -= 1
        else:
            # Идем туда, где больше значение
            if dp[i - 1][j] >= dp[i][j - 1]:
                i -= 1
            else:
                j -= 1

    # Разворачиваем, так как восстанавливали с конца
    lcs_str.reverse()

    return dp[n][m], "".join(lcs_str)

def knapsack_with_items(weights, values, capacity):
    n = len(weights)

    # Формируем DP-таблицу
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        w = weights[i - 1]
        v = values[i - 1]

        for cap in range(1, capacity + 1):
            if w > cap:
                dp[i][cap] = dp[i - 1][cap]
            else:
                dp[i][cap] = max(
                    dp[i - 1][cap],
                    dp[i - 1][cap - w] + v
                )

    # Восстановление предметов
    result_value = dp[n][capacity]
    items = []

    cap = capacity
    i = n

    while i > 0:
        # Если значение отличается от верхней строки — предмет был взят
        if dp[i][cap] != dp[i - 1][cap]:
            items.append(i - 1)  # сохраняем индекс предмета
            cap -= weights[i - 1]
        i -= 1

    items.reverse()
    return result_value, items
