# Найти количество компонент связности неориентированного графа при помощи поиска в глубину.
#
# Формат входных данных:
# На вход подаётся описание графа. В первой строке указаны два натуральных числа, разделенные пробелом: число вершин
# v \leq 1000v≤1000 и число рёбер e \leq 1000e≤1000. В следующих ee строках содержатся описания рёбер.
# Каждое ребро задаётся разделённой пробелом парой номеров вершин, которые это ребро соединяет.
# Считается, что вершины графа пронумерованы числами от 1 до vv.
#
# Формат выходных данных:
#
# Одно число — количество компонент связности графа.

def dfsGraph(k):
    curr = graph[k]
    if components[k] != -1:
        return
    components[k] = 0
    for i in range(len(curr)):
        dfsGraph(curr[i])


verticles, edges = (int(x) for x in input().split(' '))
graph = [[] for i in range(verticles)]
components = [-1 for i in range(verticles)]

for i in range(edges):
    x, y = (int(x) - 1 for x in input().split(' '))
    graph[x].append(y)
    graph[y].append(x)

j = 0
cnt = 0
for j in range(len(components)):
    if components[j] == -1:
        dfsGraph(j)
        cnt += 1
print(cnt)
