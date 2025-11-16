import matplotlib.pyplot as plt

time_data = {}

def plot_creater(sort_name, size, time_sec, data_type="random"):
    """
    sort_name : str -> название алгоритма
    size      : int -> размер массива
    time_sec  : float -> время выполнения
    data_type : str -> тип данных ("random", "sorted", etc.)
    """
    global time_data
    if data_type not in time_data:
        time_data[data_type] = {}
    if sort_name not in time_data[data_type]:
        time_data[data_type][sort_name] = {"sizes": [], "times": []}

    time_data[data_type][sort_name]["sizes"].append(size)
    time_data[data_type][sort_name]["times"].append(time_sec)

def plot_graph(data_type="random"):
    """
    Построение графика зависимости времени сортировки от размера массива
    для указанного типа данных
    """
    global time_data
    if data_type not in time_data:
        print(f"Нет данных для {data_type}")
        return

    plt.figure(figsize=(10,6))
    for sort_name, d in time_data[data_type].items():
        plt.plot(d["sizes"], d["times"], marker='o', label=sort_name)
    plt.xlabel("Размер массива")
    plt.ylabel("Время выполнения (сек)")
    plt.title(f"Время сортировки vs размер массива ({data_type})")
    plt.legend()
    plt.grid(True)
    plt.show()