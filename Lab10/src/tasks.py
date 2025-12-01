from graph_representation import AdjacencyListGraph
from shortest_path import dijkstra, connected_components, topological_sort
from graph_traversal import bfs

def practical_tasks():
    # Лабиринт (5x5)
    maze = [
        [0, 1, 0, 0, 0],
        [0, 1, 0, 1, 0],
        [0, 0, 0, 1, 0],
        [1, 1, 0, 0, 0],
        [0, 0, 0, 1, 0],
    ]
    start, end = (0,0), (4,4)
    rows, cols = len(maze), len(maze[0])
    
    def pos_to_vertex(r, c):
        return r*cols + c
    
    g_list = AdjacencyListGraph()
    for r in range(rows):
        for c in range(cols):
            if maze[r][c] == 0:
                v = pos_to_vertex(r,c)
                g_list.add_vertex(v)
                for dr, dc in [(1,0),(0,1),(-1,0),(0,-1)]:
                    nr, nc = r+dr, c+dc
                    if 0 <= nr < rows and 0 <= nc < cols and maze[nr][nc]==0:
                        g_list.add_edge(v,pos_to_vertex(nr,nc))

    distances, parents = bfs(g_list, pos_to_vertex(*start))
    path = []
    v = pos_to_vertex(*end)
    while v is not None:
        path.append(v)
        v = parents[v]
    path = path[::-1]
    print("Кратчайший путь в лабиринте (BFS):", path)
    
    # Связность сети
    cc = connected_components(g_list)
    print("Компоненты связности:", cc)
    
    # Топологическая сортировка (пример)
    g_topo = AdjacencyListGraph()
    edges = [(5,2),(5,0),(4,0),(4,1),(2,3),(3,1)]
    for u,v in edges:
        g_topo.add_vertex(u)
        g_topo.add_vertex(v)
        g_topo.add_edge(u,v)
    topo_order = topological_sort(g_topo)
    print("Топологическая сортировка:", topo_order)

if __name__ == "__main__":
    practical_tasks()