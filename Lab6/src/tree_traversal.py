from typing import Optional, List
from binary_search_tree import TreeNode

class TreeTraversal:
    """Класс с методами обхода BST"""

    @staticmethod
    def inorder_recursive(node: Optional[TreeNode], result: Optional[List[int]] = None) -> List[int]:
        """In-order обход: левое поддерево → корень → правое поддерево"""
        if result is None:
            result = []
        if node:
            TreeTraversal.inorder_recursive(node.left, result)
            result.append(node.value)
            TreeTraversal.inorder_recursive(node.right, result)
        return result

    @staticmethod
    def preorder_recursive(node: Optional[TreeNode], result: Optional[List[int]] = None) -> List[int]:
        """Pre-order обход: корень → левое поддерево → правое поддерево"""
        if result is None:
            result = []
        if node:
            result.append(node.value)
            TreeTraversal.preorder_recursive(node.left, result)
            TreeTraversal.preorder_recursive(node.right, result)
        return result

    @staticmethod
    def postorder_recursive(node: Optional[TreeNode], result: Optional[List[int]] = None) -> List[int]:
        """Post-order обход: левое поддерево → правое поддерево → корень"""
        if result is None:
            result = []
        if node:
            TreeTraversal.postorder_recursive(node.left, result)
            TreeTraversal.postorder_recursive(node.right, result)
            result.append(node.value)
        return result

    @staticmethod
    def inorder_iterative(root: Optional[TreeNode]) -> List[int]:
        """Итеративный in-order обход с использованием стека"""
        result: List[int] = []
        stack: List[TreeNode] = []
        current = root

        while stack or current:
            # Спускаемся влево до самого левого узла
            while current:
                stack.append(current)
                current = current.left

            current = stack.pop()  # Берем узел из стека
            result.append(current.value)  # Обрабатываем корень
            current = current.right  # Переходим в правое поддерево

        return result