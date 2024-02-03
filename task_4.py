import uuid
import networkx as nx
import matplotlib.pyplot as plt

class HeapNode:
    def __init__(self, key, index, color="skyblue"):
        self.left = None
        self.right = None
        self.val = key
        self.index = index
        self.color = color
        self.id = str(uuid.uuid4())

def add_heap_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.id, color=node.color, label=f"{node.val}\n({node.index})")
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2 ** layer
            pos[node.left.id] = (l, y - 1)
            l = add_heap_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2 ** layer
            pos[node.right.id] = (r, y - 1)
            r = add_heap_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph

def draw_heap(heap_root):
    heap = nx.DiGraph()
    pos = {heap_root.id: (0, 0)}
    heap = add_heap_edges(heap, heap_root, pos)

    colors = [node[1]['color'] for node in heap.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in heap.nodes(data=True)}

    plt.figure(figsize=(10, 7))
    nx.draw(heap, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)
    plt.show()

def heapify(arr, is_max_heap=True):
    nodes = [HeapNode(val, index) for index, val in enumerate(arr)]

    for i in range(len(nodes) // 2 - 1, -1, -1):
        left_child_idx = 2 * i + 1 if is_max_heap else 2 * i + 2
        right_child_idx = 2 * i + 2 if is_max_heap else 2 * i + 1

        if left_child_idx < len(nodes):
            nodes[i].left = nodes[left_child_idx]
        if right_child_idx < len(nodes):
            nodes[i].right = nodes[right_child_idx]

    return nodes[0] if nodes else None

if __name__ == "__main__":
    heap_arr_max = [4, 12, 1, 8, 3, 11, 2, 13, 9, 5, 6, 0, 10, 7, 14]
    heap_arr_max.sort(reverse=True)
    heap_root_max = heapify(heap_arr_max, is_max_heap=True)
    draw_heap(heap_root_max)

    heap_arr_min = [4, 12, 1, 8, 3, 11, 2, 13, 9, 5, 6, 0, 10, 7, 14]
    heap_arr_min.sort()
    heap_root_min = heapify(heap_arr_min, is_max_heap=False)
    draw_heap(heap_root_min)

