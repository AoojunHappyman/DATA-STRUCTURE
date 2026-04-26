class Tree:
    
    class Node:
        def __init__(self, data):
            self.data = data
            self.children = []
            self.parent = None

    def __init__(self, root_data):
        self.root = self.Node(root_data)

    # 🔹 เพิ่มลูก
    def add_child(self, parent, data):
        new_node = self.Node(data)
        new_node.parent = parent
        parent.children.append(new_node)
        return new_node

    # 🔹 แสดงผล (DFS)
    def print_tree(self, node=None, level=0):
        if node is None:
            node = self.root
        
        print(" " * level + str(node.data))
        for child in node.children:
            self.print_tree(child, level + 2)

    # 🔹 ค้นหา (DFS)
    def search(self, node, target):
        if node.data == target:
            return node
        
        for child in node.children:
            result = self.search(child, target)
            if result:
                return result
        
        return None

    # 🔹 ลบ node (ลบทั้ง subtree)
    def remove(self, node):
        if node is self.root:
            self.root = None
        else:
            parent = node.parent
            parent.children.remove(node)

    # 🔹 หาจำนวนลูก
    def num_children(self, node):
        return len(node.children)

    # 🔹 เช็ค leaf
    def is_leaf(self, node):
        return len(node.children) == 0
    
tree = Tree("A")

b = tree.add_child(tree.root, "B")
c = tree.add_child(tree.root, "C")
d = tree.add_child(tree.root, "D")

e = tree.add_child(b, "E")
f = tree.add_child(b, "F")
g = tree.add_child(c, "G")

print("Tree:")
tree.print_tree()

# ค้นหา
result = tree.search(tree.root, "F")
print("\nSearch F:", result.data if result else "Not found")

# ลบ node
tree.remove(c)

print("\nAfter removing C:")
tree.print_tree()