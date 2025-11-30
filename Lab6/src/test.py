import unittest
from binary_search_tree import BinarySearchTree
from tree_traversal import TreeTraversal

class TestBinarySearchTree(unittest.TestCase):
    def setUp(self):
        """Создание нового дерева для каждого теста"""
        self.bst = BinarySearchTree()

    def test_insert_and_search(self):
        """Тест вставки и поиска"""
        values = [10, 5, 15, 3, 7, 12, 18]
        for v in values:
            self.bst.insert(v)

        # Проверяем, что все вставленные элементы можно найти
        for v in values:
            node = self.bst.search(v)
            self.assertIsNotNone(node)
            self.assertEqual(node.value, v)

        # Проверяем поиск несуществующего элемента
        self.assertIsNone(self.bst.search(100))

        # Проверяем, что дерево остаётся корректным BST
        self.assertTrue(self.bst.is_valid_bst())

    def test_delete_leaf_node(self):
        """Удаление листового узла"""
        values = [10, 5, 15]
        for v in values:
            self.bst.insert(v)

        self.bst.delete(5)  # лист
        self.assertIsNone(self.bst.search(5))
        self.assertTrue(self.bst.is_valid_bst())

    def test_delete_node_with_one_child(self):
        """Удаление узла с одним потомком"""
        values = [10, 5, 15, 12]
        for v in values:
            self.bst.insert(v)

        self.bst.delete(15)  # узел с одним левым потомком
        self.assertIsNone(self.bst.search(15))
        self.assertTrue(self.bst.is_valid_bst())

    def test_delete_node_with_two_children(self):
        """Удаление узла с двумя потомками"""
        values = [10, 5, 15, 12, 18]
        for v in values:
            self.bst.insert(v)

        self.bst.delete(15)  # узел с двумя потомками
        self.assertIsNone(self.bst.search(15))
        self.assertTrue(self.bst.is_valid_bst())

    def test_inorder_traversal_sorted(self):
        """In-order traversal должен возвращать отсортированный список"""
        values = [10, 5, 15, 3, 7, 12, 18]
        for v in values:
            self.bst.insert(v)

        sorted_values = sorted(values)
        traversal_result = TreeTraversal.inorder_recursive(self.bst.root)
        self.assertEqual(traversal_result, sorted_values)

    def test_height(self):
        """Проверка высоты дерева"""
        values = [10, 5, 15, 3, 7, 12, 18]
        for v in values:
            self.bst.insert(v)

        h = self.bst.height()
        # Высота сбалансированного дерева из 7 узлов = 3
        self.assertEqual(h, 3)

if __name__ == "__main__":
    unittest.main(argv=[''], exit=False, verbosity=2)
