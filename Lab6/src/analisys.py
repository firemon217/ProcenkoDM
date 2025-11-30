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

    # Дополнительно можно реализовать обход дерева для проверки:
    def inorder_traversal(self, node: Optional[TreeNode] = None, result=None):
        """In-order обход (возвращает отсортированный список значений)"""
        if result is None:
            result = []
        if node is None:
            node = self.root
        if node.left:
            self.inorder_traversal(node.left, result)
        result.append(node.value)
        if node.right:
            self.inorder_traversal(node.right, result)
        return result