import unittest
import time
import matplotlib.pyplot as plt
import numpy as np
from itertools import product
from hash_functions import *
from hash_table_openaddressing import *
from hash_table_chaining import *

class TestHashTables(unittest.TestCase):
    
    def setUp(self):
        """Инициализация тестовых данных"""
        self.test_data = [
            ("key1", "value1"),
            ("key2", "value2"), 
            ("key3", "value3"),
            ("key4", "value4"),
            ("key5", "value5"),
            ("collision_key", "collision_value")  # Для теста коллизий
        ]
        
    def test_basic_operations(self):
        """Тест базовых операций для всех реализаций хеш-таблиц"""
        implementations = [HashTableChaining, HashTableLinear, HashTableDoubleHash]
        
        for impl in implementations:
            with self.subTest(implementation=impl.__name__):
                ht = impl(size=4)  # Маленький размер для теста коллизий
                
                # Тест вставки
                for key, value in self.test_data:
                    ht.insert(key, value)
                
                # Тест поиска
                for key, expected_value in self.test_data:
                    self.assertEqual(ht.search(key), expected_value)
                
                # Тест обновления значения
                ht.insert("key1", "updated_value")
                self.assertEqual(ht.search("key1"), "updated_value")
                
                # Тест удаления
                self.assertTrue(ht.delete("key1"))
                self.assertIsNone(ht.search("key1"))
                self.assertFalse(ht.delete("nonexistent_key"))
    
    def test_collision_handling(self):
        """Тест обработки коллизий"""
        # Создаем ключи, которые гарантированно вызовут коллизии
        collision_keys = ["a", "b", "c", "d", "e", "f", "g"]
        
        implementations = [HashTableChaining, HashTableLinear, HashTableDoubleHash]
        
        for impl in implementations:
            with self.subTest(implementation=impl.__name__):
                ht = impl(size=3)  # Очень маленький размер для принудительных коллизий
                
                # Вставляем все ключи
                for i, key in enumerate(collision_keys):
                    ht.insert(key, f"value{i}")
                
                # Проверяем, что все значения доступны
                for i, key in enumerate(collision_keys):
                    self.assertEqual(ht.search(key), f"value{i}")
    
    def test_resize_operation(self):
        """Тест операции изменения размера"""
        implementations = [HashTableChaining, HashTableLinear, HashTableDoubleHash]
        
        for impl in implementations:
            with self.subTest(implementation=impl.__name__):
                ht = impl(size=2)  # Начинаем с очень маленького размера
                
                # Вставляем больше элементов, чем начальный размер
                for i in range(10):
                    ht.insert(f"key{i}", f"value{i}")
                
                # Проверяем, что все значения доступны после resize
                for i in range(10):
                    self.assertEqual(ht.search(f"key{i}"), f"value{i}")
                
                # Проверяем, что размер увеличился
                self.assertGreater(ht.size, 2)

class HashTableBenchmark:
    """Класс для benchmarking хеш-таблиц"""
    
    def __init__(self):
        self.implementations = [HashTableChaining, HashTableLinear, HashTableDoubleHash]
        self.load_factors = [0.1, 0.5, 0.7, 0.9]
        self.operations = ['insert', 'search', 'delete']
        
    def generate_test_data(self, size):
        """Генерация тестовых данных"""
        return [(
            f"key_{i}", 
            f"value_{i}"
        ) for i in range(size)]
    
    def measure_operation_time(self, implementation, load_factor, operation, data_size=10000):
        """Измерение времени выполнения операции"""
        # Вычисляем размер таблицы для достижения нужного коэффициента заполнения
        table_size = int(data_size / load_factor)
        ht = implementation(size=table_size)
        test_data = self.generate_test_data(data_size)
        
        # Предварительно заполняем таблицу
        for key, value in test_data[:int(data_size * load_factor)]:
            ht.insert(key, value)
        
        # Измеряем время выполнения операции
        start_time = time.time()
        
        if operation == 'insert':
            # Вставляем оставшиеся элементы
            for key, value in test_data[int(data_size * load_factor):]:
                ht.insert(key, value)
        elif operation == 'search':
            # Ищем все элементы
            for key, _ in test_data[:int(data_size * load_factor)]:
                ht.search(key)
        elif operation == 'delete':
            # Удаляем половину элементов
            for key, _ in test_data[:int(data_size * load_factor) // 2]:
                ht.delete(key)
        
        end_time = time.time()
        return end_time - start_time
    
    def run_benchmarks(self):
        """Запуск всех benchmark тестов"""
        results = {}
        
        for impl, load_factor, operation in product(self.implementations, self.load_factors, self.operations):
            impl_name = impl.__name__
            if impl_name not in results:
                results[impl_name] = {}
            if operation not in results[impl_name]:
                results[impl_name][operation] = []
                
            time_taken = self.measure_operation_time(impl, load_factor, operation)
            results[impl_name][operation].append((load_factor, time_taken))
            
            print(f"{impl_name} - Load factor: {load_factor} - {operation}: {time_taken:.6f}s")
        
        return results
    
    def plot_performance(self, results):
        """Построение графиков производительности"""
        fig, axes = plt.subplots(1, 3, figsize=(15, 5))
        
        for idx, operation in enumerate(self.operations):
            ax = axes[idx]
            for impl_name in results:
                load_factors = [lf for lf, _ in results[impl_name][operation]]
                times = [t for _, t in results[impl_name][operation]]
                ax.plot(load_factors, times, marker='o', label=impl_name)
            
            ax.set_title(f'Time vs Load Factor - {operation.capitalize()}')
            ax.set_xlabel('Load Factor')
            ax.set_ylabel('Time (seconds)')
            ax.legend()
            ax.grid(True)
        
        plt.tight_layout()
        plt.savefig('hash_table_performance.png', dpi=300, bbox_inches='tight')
        plt.show()
    
    def analyze_collisions(self, hash_functions, test_size=1000, table_size=100):
        """Анализ коллизий для разных хеш-функций"""
        collision_stats = {}
        
        for func_name, hash_func in hash_functions.items():
            hash_values = []
            test_data = self.generate_test_data(test_size)
            
            for key, _ in test_data:
                hash_val = hash_func(key, table_size)
                hash_values.append(hash_val)
            
            # Анализ распределения
            unique_hashes = len(set(hash_values))
            collisions = test_size - unique_hashes
            collision_rate = collisions / test_size
            
            collision_stats[func_name] = {
                'collisions': collisions,
                'collision_rate': collision_rate,
                'distribution': hash_values
            }
            
            print(f"{func_name}: {collisions} collisions ({collision_rate:.2%})")
        
        return collision_stats
    
    def plot_collision_distribution(self, collision_stats):
        """Построение гистограмм распределения коллизий"""
        fig, axes = plt.subplots(2, 2, figsize=(12, 10))
        axes = axes.flatten()
        
        for idx, (func_name, stats) in enumerate(collision_stats.items()):
            if idx >= len(axes):
                break
                
            ax = axes[idx]
            distribution = stats['distribution']
            
            ax.hist(distribution, bins=50, alpha=0.7, edgecolor='black')
            ax.set_title(f'{func_name}\nCollisions: {stats["collisions"]} ({stats["collision_rate"]:.2%})')
            ax.set_xlabel('Hash Value')
            ax.set_ylabel('Frequency')
            ax.grid(True, alpha=0.3)
        
        plt.tight_layout()
        plt.savefig('hash_function_collisions.png', dpi=300, bbox_inches='tight')
        plt.show()

def custom_hash_simple(key, size):
    """Простая хеш-функция для сравнения"""
    return sum(ord(c) for c in key) % size

def custom_hash_poly(key, size):
    """Полиномиальная хеш-функция"""
    p = 31
    hash_val = 0
    for c in key:
        hash_val = hash_val * p + ord(c)
    return hash_val % size

# Запуск тестов и benchmark
if __name__ == "__main__":
    # Запуск unit-тестов
    unittest.main(argv=[''], exit=False, verbosity=2)
    
    # Benchmark тесты
    benchmark = HashTableBenchmark()
    
    print("\n" + "="*50)
    print("RUNNING PERFORMANCE BENCHMARKS")
    print("="*50)
    
    # Тесты производительности
    performance_results = benchmark.run_benchmarks()
    benchmark.plot_performance(performance_results)
    
    print("\n" + "="*50)
    print("ANALYZING HASH FUNCTION COLLISIONS")
    print("="*50)
    
    # Анализ коллизий хеш-функций
    hash_functions = {
        'Built-in hash': lambda k, s: hash(k) % s,
        'Simple sum': custom_hash_simple,
        'Polynomial': custom_hash_poly,
        'DJB2': lambda k, s: hash_djb2(k, s)
    }
    
    collision_stats = benchmark.analyze_collisions(hash_functions)
    benchmark.plot_collision_distribution(collision_stats)
    
    # Анализ результатов
    print("\n" + "="*50)
    print("PERFORMANCE ANALYSIS SUMMARY")
    print("="*50)
    
    for impl_name in performance_results:
        print(f"\n{impl_name}:")
        for operation in benchmark.operations:
            times = [t for _, t in performance_results[impl_name][operation]]
            best_lf = benchmark.load_factors[np.argmin(times)]
            print(f"  {operation}: Best load factor = {best_lf}")

# Дополнительные функции для анализа
def analyze_optimal_load_factors(performance_results):
    """Анализ оптимальных коэффициентов заполнения"""
    optimal_factors = {}
    
    for impl_name in performance_results:
        optimal_factors[impl_name] = {}
        for operation in ['insert', 'search', 'delete']:
            times = [t for _, t in performance_results[impl_name][operation]]
            optimal_idx = np.argmin(times)
            optimal_factors[impl_name][operation] = benchmark.load_factors[optimal_idx]
    
    return optimal_factors

def compare_implementation_efficiency(performance_results):
    """Сравнение эффективности реализаций"""
    efficiency_scores = {}
    
    for impl_name in performance_results:
        total_score = 0
        for operation in benchmark.operations:
            times = [t for _, t in performance_results[impl_name][operation]]
            # Чем меньше время, тем выше score
            score = 1 / np.mean(times)
            total_score += score
        
        efficiency_scores[impl_name] = total_score
    
    return efficiency_scores