from collections import deque

def bfs(graph,start):
    visited = set()
    queue = deque([start])
    result = []
    
    while queue:
        node = queue.popleft()
        if node not in visited:
            result.append(node)
            visited.add(node)
            
            for neighbor in graph.get(node,[]):
                if neighbor not in visited:
                    queue.append(neighbor)
    return result


def depthft(graph,start):
    
    visited = set()
    result = []
    
    def dfs(node):
        if node in visited:
            return
        
        visited.add(node)
        result.append(node)
        
        for nb in graph.get(node,[]):
            dfs(nb)
            
    dfs(start)
    return result

def list_to_matrix(graph):
    # 1. เก็บชื่อ node ทั้งหมด
    nodes = list(graph.keys())

    # เผื่อมี node ที่อยู่ใน value แต่ไม่มี key (เช่น S)
    for neighbors in graph.values():
        for n in neighbors:
            if n not in nodes:
                nodes.append(n)

    nodes.sort()  # เรียงให้สวย (optional)

    # 2. สร้าง matrix n x n (เริ่มด้วย 0)
    size = len(nodes)
    matrix = [[0] * size for _ in range(size)]

    # 3. map node → index
    index = {node: i for i, node in enumerate(nodes)}

    # 4. ใส่ค่า edge
    for u in graph:
        for v in graph[u]:
            i = index[u]
            j = index[v]
            matrix[i][j] = 1

    return nodes, matrix

graph = {
    'A' : ['B','C'],
    'B' : ['A','D'],
    'C' : ['A','B','D'],
    'D' : ['B','C'],
    'E' : ['A','C']
}

graph2 = {
    'A' : ['B','S'],
    'B' : ['A'],
    'C' : ['D','E','F','S'],
    'E' : ['C','H'],
    'F' : ['C','G'],
    'G' : ['F','S','H'],
    'H' : ['E','G']
}

print(bfs(graph2,'C'))
print(depthft(graph2,'C'))
print(list_to_matrix(graph2))