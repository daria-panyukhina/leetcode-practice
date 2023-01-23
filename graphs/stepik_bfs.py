# На вход программе подаётся описание простого связного графа. Первая строка содержит два числа:
# число вершин V≤10000 и число рёбер E≤30000 графа.
# Следующие E строк содержат номера пар вершин, соединенных рёбрами.
# Вершины имеют номера от 0 до V-1. Выведите список из VV чисел — расстояний
# от вершины 0 до соответствующих вершин графа.

from collections import deque


def myBFS(k):
    queue = deque()
    queue.append(k)
    dist[k] = 0
    while queue:
        curr = queue.popleft()
        children = graph[curr]
        for child in children:
            if dist[child] == -1:
                dist[child] = dist[curr] + 1
                queue.append(child)


verticles, edges = (int(x) for x in input().split((' ')))
graph = [[] for i in range(verticles)]
dist = [-1 for i in range(verticles)]


for i in range(edges):
    x, y = (int(x) for x in input().split(' '))
    graph[x].append(y)
    graph[y].append(x)

# graph = [[1, 2], [0, 2], [1, 0, 3, 4], [2, 4], [3, 2, 5], [4]]
# dist = [-1, -1, -1, -1, -1, -1]
myBFS(0)
print(*dist)
