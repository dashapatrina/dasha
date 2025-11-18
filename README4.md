
# Практическое задание №1.4: Структуры данных («Деревья/графы») 


### Древовидные структуры (Trees)
**Древовидная структура** представляет собой нелинейную структуру данных, состоящую из узлов (vertices), соединённых направленными дугами (edges). Каждый узел может иметь нулевое или большее количество дочерних узлов, образуя иерархию.

Основные типы деревьев:
- **Бинарное дерево**: каждый узел имеет максимум два дочерних узла (левый и правый ребёнок).
- **N-арное дерево**: узел может иметь любое количество дочерних узлов.

Операции над деревьями включают:
- вставку новых узлов;
- удаление существующих узлов;
- поиск определённого узла;
- вычисление глубины дерева;
- обход дерева различными методами (preorder, inorder, postorder, depth-first search, breadth-first search).

### Графовые структуры (Graphs)
**Граф** — это абстрактная структура данных, представляющая собой совокупность множества вершин (nodes) и множеств связей (edges) между ними. Связи могут быть направлены (directed graphs) или ненаправленные (undirected graphs).

Типичные операции с графами:
- поиск пути между двумя вершинами;
- определение наличия цикла;
- нахождение кратчайшего пути (алгоритм Дейкстры, Bellman-Ford);
- нахождение минимального покрывающего дерева (Prim's algorithm, Kruskal's algorithm).

---

## Примеры заданий и решений

### Задача 1: Поиск пути в дереве (DFS)
Цель: реализовать поиск пути от корня дерева до заданного узла методом Depth First Search (DFS).

#### Решение:
Используется рекурсивный обход дерева в глубину (DFS). Алгоритм проходит по каждому узлу дерева, сохраняя пройденный путь и проверяя, достигнута ли цель.

```python
class Node:
    def __init__(self, value):
        self.value = value
        self.children = []
    
    def add_child(self, child_node):
        self.children.append(child_node)

def find_path(root, target):
    path = []
    if dfs_find_path(root, target, path):
        return path
    return None

def dfs_find_path(node, target, path):
    if node is None:
        return False
    path.append(node.value)
    if node.value == target:
        return True
    for child in node.children:
        if dfs_find_path(child, target, path):
            return True
    path.pop()
    return False

# Пример использования
root = Node('A')
b = Node('B'); c = Node('C'); d = Node('D'); e = Node('E')
root.add_child(b); root.add_child(c)
b.add_child(d); b.add_child(e)
c.add_child(Node('F'))
d.add_child(Node('G')); e.add_child(Node('H'))

target_value = 'H'
result_path = find_path(root, target_value)
if result_path:
    print("Путь:", result_path)
```

#### Объяснение шагов:
1. Определяем классы `Node` для представления узлов дерева.
2. Метод `find_path()` инициирует процесс поиска путём запуска рекурсивной функции `dfs_find_path`.
3. Рекурсия продолжается до тех пор, пока не будет достигнут целевой узел (`target`), после чего возвращается успешный результат.
4. После завершения рекурсии возвращаются промежуточные результаты поиска, формирующие путь.

---

### Задача 2: Нахождение кратчайшего пути в графе (Алгоритм Дейкстры)
Цель: реализовать поиск кратчайшего пути между двумя вершинами графа с использованием алгоритма Дейкстры.

#### Решение:
Алгоритм Дейкстры основан на поиске кратчайших путей от одной вершины ко всем остальным вершинам в графе. Используется очередь с приоритетами для эффективного выбора следующего шага.

```python
import heapq

def dijkstra(graph, start):
    distances = {vertex: float('inf') for vertex in graph}
    distances[start] = 0
    priority_queue = [(0, start)]

    while priority_queue:
        current_dist, current_vertex = heapq.heappop(priority_queue)
        if current_dist > distances[current_vertex]:
            continue
        
        for neighbor, weight in graph[current_vertex].items():
            dist = current_dist + weight
            if dist < distances[neighbor]:
                distances[neighbor] = dist
                heapq.heappush(priority_queue, (dist, neighbor))
    
    return distances

# Пример использования
graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1}
}

start_vertex = 'A'
result = dijkstra(graph, start_vertex)
print(result)
```

#### Объяснение шагов:
1. Используем модуль `heapq`, обеспечивающий эффективную реализацию приоритета очереди (кучи).
2. Начальные расстояния устанавливаются в бесконечность для всех вершин, кроме начальной (`start`), для которой устанавливается расстояние 0.
3. Алгоритм последовательно выбирает вершины с наименьшими известными расстояниями, обновляя пути и записывая новые минимальные расстояния.
4. Итоговый результат — это словарь с кратчайшими расстояниями от начальной вершины до всех остальных.

