import uuid
from collections import deque
import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.colors import to_rgba, to_hex

class TreeNode:
    def __init__(self, key, color="#1296F0"):
        self.left = None
        self.right = None
        self.val = key
        self.base_color = color
        self.color = color
        self.id = str(uuid.uuid4())

def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val)
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2**layer
            pos[node.left.id] = (l, y - 1)
            add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2**layer
            pos[node.right.id] = (r, y - 1)
            add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph

def draw_tree(tree_root):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)

    colors = {node[0]: node[1]["color"] for node in tree.nodes(data=True)}
    labels = {node[0]: f"{node[1]['label']}\nColor: {colors[node[0]]}" for node in tree.nodes(data=True)}

    plt.figure(figsize=(8, 5))
    nx.draw(
        tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=list(colors.values())
    )
    plt.show()

def dfs_path(node, base_color, visited=set()):
    if node is not None:
        visited.add(node.id)
        node.color = get_color(base_color, len(visited))
        dfs_path(node.left, base_color, visited)
        dfs_path(node.right, base_color, visited)

def bfs_path(root, base_color, visited=set()):
    if root is not None:
        queue = [root]
        while queue:
            node = queue.pop(0)
            if node.id not in visited:
                visited.add(node.id)
                node.color = get_color(base_color, len(visited))
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

def get_color(base_color, index, step=15):
    rgb_color = to_rgba(base_color)[:-1]
    lightened_rgb = tuple(min(1.0, c + index * step / 255.0) for c in rgb_color)
    lightened_hex = to_hex(lightened_rgb)
    return lightened_hex

if __name__ == "__main__":
    root = TreeNode(0)
    root.left = TreeNode(1)
    root.right = TreeNode(2)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(4)
    root.right.left = TreeNode(5)
    root.right.right = TreeNode(6)
    root.left.left.left = TreeNode(7)
    root.left.left.right = TreeNode(8)
    root.left.right.left = TreeNode(9)
    root.left.right.right = TreeNode(10)
    root.right.left.left = TreeNode(11)
    root.right.left.right = TreeNode(12)
    root.right.right.left = TreeNode(13)
    root.right.right.right = TreeNode(14)

    dfs_path(root, root.base_color)
    draw_tree(root)

    bfs_path(root, root.base_color)
    draw_tree(root)
