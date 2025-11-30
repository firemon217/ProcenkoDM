from typing import Optional

class TreeNode:
    """Узел бинарного дерева поиска (BST)"""
    def __init__(self, value):
        self.value = value          # Значение узла
        self.left: Optional['TreeNode'] = None   # Левый потомок
        self.right: Optional['TreeNode'] = None  # Правый потомок

class BinarySearchTree:
    """Класс бинарного дерева поиска (BST)"""
    def __init__(self):
        self.root: Optional[TreeNode] = None  # Корень дерева

    def insert(self, value):
        """Вставка нового значения в BST"""
        if self.root is None:
            # Если дерево пустое, создаем корень
            self.root = TreeNode(value)
            return

        current = self.root
        while True:
            if value < current.value:
                # Идем в левое поддерево
                if current.left is None:
                    current.left = TreeNode(value)
                    return
                current = current.left
            elif value > current.value:
                # Идем в правое поддерево
                if current.right is None:
                    current.right = TreeNode(value)
                    return
                current = current.right
            else:
                # Значение уже есть — игнорируем или обновляем (в BST обычно уникальные ключи)
               return
    # Средний	O(log n) — дерево сбалансировано, высота ~ log n
    # Худший	O(n) — дерево вырождено (список)

    def search(self, value) -> Optional[TreeNode]:
        """Поиск узла с заданным значением"""
        current = self.root
        while current:
            if value < current.value:
                current = current.left
            elif value > current.value:
                current = current.right
            else:
                return current  # Найдено
        return None  # Не найдено
    # Средний	O(log n)
    # Худший	O(n)

    def find_min(self, node: Optional[TreeNode]) -> Optional[TreeNode]:
        """Поиск узла с минимальным значением в поддереве"""
        if node is None:
            return None
        current = node
        while current.left:
            current = current.left
        return current
    # Средний	O(log n)
    # Худший	O(n)

    def find_max(self, node: Optional[TreeNode]) -> Optional[TreeNode]:
        """Поиск узла с максимальным значением в поддереве"""
        if node is None:
            return None
        current = node
        while current.right:
            current = current.right
        return current
    # Средний	O(log n)
    # Худший	O(n)

    def delete(self, value):
        """Удаление узла с заданным значением"""
        self.root = self._delete_rec(self.root, value)
    # Средний	O(log n)
    # Худший	O(n)

    def _delete_rec(self, node: Optional[TreeNode], value) -> Optional[TreeNode]:
        """Рекурсивная функция удаления узла"""
        if node is None:
            return None

        if value < node.value:
            node.left = self._delete_rec(node.left, value)
        elif value > node.value:
            node.right = self._delete_rec(node.right, value)
        else:
            # Найден узел для удаления
            if node.left is None:
                return node.right  # Если нет левого потомка — возвращаем правого
            elif node.right is None:
                return node.left   # Если нет правого потомка — возвращаем левого
            else:
                # Узел имеет двух потомков — ищем минимальный элемент в правом поддереве
                min_larger_node = self.find_min(node.right)
                node.value = min_larger_node.value  # Копируем значение
                node.right = self._delete_rec(node.right, min_larger_node.value)  # Удаляем дубликат

        return node
    
    def is_valid_bst(self, node: Optional[TreeNode] = None, min_val=float('-inf'), max_val=float('inf')) -> bool:
        """
        Проверка, является ли дерево корректным BST.
        Используется рекурсивный обход с ограничениями на значения узлов.
        """
        if node is None:
            node = self.root
        if node is None:
            return True  # Пустое дерево — корректный BST

        if not (min_val < node.value < max_val):
            return False  # Нарушение свойства BST

        # Проверяем левое и правое поддеревья с обновлёнными ограничениями
        return (self.is_valid_bst(node.left, min_val, node.value) and
                self.is_valid_bst(node.right, node.value, max_val))

    def height(self, node: Optional[TreeNode] = None) -> int:
        """
        Вычисление высоты дерева или поддерева.
        Высота пустого дерева = 0, листья = 1
        """
        if node is None:
            node = self.root
        if node is None:
            return 0

        left_height = self.height(node.left)
        right_height = self.height(node.right)

        return 1 + max(left_height, right_height)