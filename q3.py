# ONLY EDIT FUNCTIONS MARKED CLEARLY FOR EDITING

import numpy as np
import operator

def question03(numNodes, edgeList):
  # modify and then return the variable below
  answer = -1
  colorationList = coloration(numNodes, edgeList)
  nb_colors = dict()
  for color in colorationList:
    if color not in nb_colors:
      nb_colors[color] = 1
    else:
      nb_colors[color] += 1
  nb_colors_sorted = sorted(nb_colors.items(), key=operator.itemgetter(1), reverse = True)
  # couleur qui apparait le plus est: nb_colors_sorted[0][0]
  X = nb_colors_sorted[0][1]
  Y = numNodes - X
  answer = X - Y
  return answer

def coloration(numNodes, edgeList):
  # modify and then return the variable below
  answer = -1
  nodeList = [i+1 for i in range(numNodes)]
  d = dict()
  for node in nodeList:
    d[node] = []
    for elt in edgeList:
      if elt[0] == node:
        d[node].append(elt[1])
      if elt[1] == node:
        d[node].append(elt[0])
  degreDict = dict()
  for node in nodeList:
    degreDict[node] = len(d[node])
  degreSorted = sorted(degreDict.items(), key=operator.itemgetter(1), reverse = True)
  # Coloration
  currentColor = 1
  coloration = [0 for node in nodeList]
  nonVisited = [node for node in nodeList]
  coloration[degreSorted[0][0]-1] = 1 # premier sommet colore
  nonVisited.remove(degreSorted[0][0])
  
  while len(nonVisited) > 0:
    # Find highest DSAT in nonVisited
    DSATList = []
    for node in nonVisited:
      DSATList.append((node, DSAT(node, d, coloration)))
    DSATList = sorted(DSATList, key = func, reverse = True)
    highest_DSAT = DSATList[0][1]
    potential_nodes = [] # Tous les noeuds ayant le max DSAT
    for elt in DSATList:
      if elt[1] == highest_DSAT:
        potential_nodes.append(elt[0])
    # si highest_DSAT unique alors c'est le noeud a colorer
    if len(potential_nodes) == 1:
      node_to_color = potential_nodes[0]
    # prendre celui au plus haut degre
    else:
      highest_degre = 0
      node_to_color = 0
      for node in potential_nodes:
        if degreDict[node] > highest_degre:
          highest_degre = degreDict[node]
          node_to_color = node
    # trouver la coloration minimale a ce noeud
    voisins_node_to_color = d[node_to_color]
    color = 1
    # faut la liste des couleurs des voisins
    voisins_color_list = []
    for node in voisins_node_to_color:
      voisins_color_list.append(coloration[node-1])
    while color in voisins_color_list:
      color += 1
    coloration[node_to_color-1] = color
    nonVisited.remove(node_to_color)
  return coloration

def DSAT(node, edgeDict, coloration):
  uniqueColor = []
  for elt in edgeDict[node]:
    uniqueColor.append(coloration[elt-1])
  uniqueColor = set(uniqueColor)
  return len(uniqueColor)

def func(x):
  return x[1]
