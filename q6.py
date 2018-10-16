# ONLY EDIT FUNCTIONS MARKED CLEARLY FOR EDITING

import numpy as np

def question06(numServers, targetServer, times):
  # modify and then return the variable below
  answer = -1
  sommetList = [i for i in range(numServers)]
  # infinity is the sum of every time in the graph
  infinity = sum([sum(l) for l in times])
  graph = times
  djikstra = [infinity for _ in range(numServers)]
  # lets visit the first node
  djikstra[0] = graph[0][0]
  visited = [0]
  for node in sommetList:
      if node not in visited:
        djikstra[node] = min(djikstra[node], djikstra[0] + graph[0][node])
  # find the node
  while len(visited) < numServers:
    nextNode = findNextNode(djikstra, visited, infinity)
    visited.append(nextNode)
    # Pour chaque sommet B not in visited voisin de nextNode
    for node in sommetList:
      if node not in visited:
        djikstra[node] = min(djikstra[node], djikstra[nextNode] + graph[nextNode][node])
  answer = djikstra[targetServer]
  return answer

def findNextNode(djikstra, visited, infinity):
  nextNode = djikstra.index(min(djikstra))
  if nextNode not in visited:
    return nextNode
  djikstraTmp = djikstra[:]
  djikstraTmp[nextNode] = infinity
  return findNextNode(djikstraTmp, visited, infinity)
