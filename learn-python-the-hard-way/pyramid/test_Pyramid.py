graph3 = {3: [1], 4: [1, 2], 5: [2], 1: [0], 2: [0]}
graph4 = {3: [1], 4: [1, 2], 5: [2], 1: [0], 2: [0], 6: [3], 7: [3, 4], 8: [4, 5], 9: [5]}
graph = graph4
    
def find_path(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return path
    if not graph.has_key(start):
        return None
    for node in graph[start]:
        if node not in path:
            newpath = find_path(graph, node, end, path)
            if newpath: return newpath
    return None
    
def find_all_paths(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return [path]
    if not graph.has_key(start):
        return []
    paths = []
    for node in graph[start]:
        if node not in path:
            newpaths = find_all_paths(graph, node, end, path)
            for newpath in newpaths:
                paths.append(newpath)
    return paths
        
# a = Pyramid(2)
# print find_path(graph, 4, 0)
# print path
print find_all_paths(graph, 7, 0)