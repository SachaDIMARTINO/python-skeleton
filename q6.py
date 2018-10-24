# ONLY EDIT FUNCTIONS MARKED CLEARLY FOR EDITING

def question06(numServers, targetServer, times):
  # modify and then return the variable below
  answer = -1
  # last update: if numServers > len(times)
  if numServers == 0 or numServers > len(times):
    return answer
  return lengthPath(targetServer, times, times[targetServer][0])

def lengthPath(startingNode, graph, minValue, visited = []):
    for i in range(len(graph)):
        graph[i][i] = 2**16
    if startingNode == 0:
        return 0
    visited.append(startingNode)
    availableNodes = []
    for i in range(len(graph[startingNode])):
        if i not in visited and graph[startingNode][i] <= minValue:
            availableNodes.append(i)
    for node in availableNodes:
        minValue = min(minValue, graph[startingNode][node] + lengthPath(node, graph, minValue, visited))
    return minValue
