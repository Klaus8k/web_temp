from collections import deque

graph = {}
graph['you'] = ['alice', 'bob', 'claire']
graph['bob'] = ['anju', 'peggy']
graph['alice'] = ['peggy']
graph['claire'] = ['thom', 'jonny']
graph['anju'] = []
graph['peggy'] = []
graph['thom'] = []
graph['jonny'] = []

def mango_seller_search(name):
    search_queue = deque()
    search_queue += graph[name]
    searched = []
    while search_queue:
        person = search_queue.popleft()
        if not person in searched:
            if person[-1] == 'y':
                print(person + ' - mango seller')
                return True
            else:
                search_queue += graph[person]
                searched.append(person)
    return False

mango_seller_search('you')


# Взвешенный граф
graph = {'start': {'a': 6, 'b': 2}, 'a': {'fin': 1}, 'b': {'a': 3, 'fin': 5}, 'fin': {}}
costs = {'a': 6, 'b': 2, 'fin': float('inf')}
parents = {'a': 'start', 'b': 'start', 'fin': None}






processed = []

def lowest_cost_node(costs):
    lower = float('inf')
    lower_node = None
    for i in costs.keys():
        if costs[i] < lower and i not in processed:
            lower = costs[i]
            lower_node = i
    return lower_node


node = lowest_cost_node(costs) # вершина с минимальным весом от начала(весом пути)
while node is not None: # Пока все не обошли
    print(node)
    cost = costs[node] # мин путь к этой точке
    neighbors = graph[node] # его соседи
    for n in neighbors.keys(): # перебор соседей
        new_cost = cost + neighbors[n] # новый путь = мин путь + путь до соседа
        if costs[n] > new_cost: # Если новый путь меньше, чем путь соседа с начала
            costs[n] = new_cost # То Через точку соседа(А) быстрее, присваиваем ей путь от начала
            parents[n] = node # и родителем соседа(А) ставим опорную точку Ноду. так как путеь будет через А
    processed.append(node) # Отмечаем в пройденных вершинах
    node = lowest_cost_node(costs) # Следующий меньший путь в необработанных


print(graph)
print(costs)
print(parents)

