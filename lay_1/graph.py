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
graph = {}
graph['start'] = {}
graph['start']['a'] = 6
graph['start']['b'] = 2
graph['a'] = {}
graph['a']['fin'] = 1
graph['b'] = {}
graph['b']['fin'] = 5
graph['b']['a'] = 3
graph['fin'] = {}

ifinity = float('inf')
costs = {}
costs['a'] = 6
costs['b'] = 2
costs['fin'] = ifinity

parents = {}
parents['a'] = 'start'
parents['b'] = 'start'
parents['fin'] = None

processed = []




print(graph)