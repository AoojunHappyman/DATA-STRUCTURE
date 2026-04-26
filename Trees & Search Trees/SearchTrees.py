
from collections import deque



class Tree:
    class Node:
        def __init__(self, data):
            self.data = data
            self.left = None
            self.right = None

    def __init__(self):
        self.root = None

    # ---------------------------
    # 🔹 INSERT (BST)
    # ---------------------------
    def insert(self, data):
        if self.root is None:
            self.root = self.Node(data)
        else:
            self._insert(self.root, data)

    def _insert(self, node, data):
        if data < node.data:
            if node.left is None:
                node.left = self.Node(data)
            else:
                self._insert(node.left, data)
        else:
            if node.right is None:
                node.right = self.Node(data)
            else:
                self._insert(node.right, data)

    # ---------------------------
    # 🔹 SEARCH (Binary Tree - DFS)
    # ---------------------------
    def search_dfs(self, key):
        return self._search_dfs(self.root, key)

    def _search_dfs(self, node, key):
        if node is None:
            return False
        if node.data == key:
            return True
        return self._search_dfs(node.left, key) or self._search_dfs(node.right, key)

    # ---------------------------
    # 🔹 SEARCH (Binary Tree - BFS)
    # ---------------------------
    def search_bfs(self, key):
        if self.root is None:
            return False
        
        queue = deque([self.root])
        while queue:
            node = queue.popleft()
            if node.data == key:
                return True
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return False

    # ---------------------------
    # 🔹 SEARCH (BST - Recursive)
    # ---------------------------
    def search_bst(self, key):
        return self._search_bst(self.root, key)

    def _search_bst(self, node, key):
        if node is None:
            return False
        if node.data == key:
            return True
        if key < node.data:
            return self._search_bst(node.left, key)
        else:
            return self._search_bst(node.right, key)

    # ---------------------------
    # 🔹 SEARCH (BST - Loop)
    # ---------------------------
    def search_bst_loop(self, key):
        node = self.root
        while node:
            if key == node.data:
                return True
            elif key < node.data:
                node = node.left
            else:
                node = node.right
        return False


# ---------------------------
# 🧪 ตัวอย่างใช้งาน
# ---------------------------
tree = Tree()

# insert แบบ BST
for x in [10, 5, 20, 3, 7, 15]:
    tree.insert(x)

print(tree.search_dfs(7))        # True
print(tree.search_bfs(15))       # True
print(tree.search_bst(20))       # True
print(tree.search_bst_loop(99))  # False