import random

def generate_datasets(sizes):
    datasets = {}

    for n in sizes:
        random_arr = [random.randint(0, n) for _ in range(n)]
        sorted_arr = sorted(random_arr)
        reversed_arr = sorted_arr[::-1]
        almost_sorted = sorted_arr.copy()
        k = n // 20
        for _ in range(k):
            i = random.randint(0, n - 1)
            j = random.randint(0, n - 1)
            almost_sorted[i], almost_sorted[j] = almost_sorted[j], almost_sorted[i]
        datasets[n] = {
            "random": random_arr,
            "sorted": sorted_arr,
            "reversed": reversed_arr,
            "almost_sorted": almost_sorted
        }

    return datasets
    