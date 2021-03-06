# ONLY EDIT FUNCTIONS MARKED CLEARLY FOR EDITING

import numpy as np

def question03(numNodes, edgeList):
  # modify and then return the variable below
  answer = -1
  colorationList = coloration(numNodes, edgeList)
  color = 1
  colorNumberList = []
  while color in colorationList:
    colorNumberList.append(colorationList.count(color))
    color += 1
  # maxColor = couleur la plus presente
  maxColor = colorNumberList.index(max(colorNumberList)) + 1
  X = max(colorNumberList)
  TE = []
  NTE = []
  for node in range(numNodes):
    if colorationList[node] == maxColor:
      TE.append(node)
    else:
      NTE.append(node)

  # Besoin de connaitre les voisins des noeuds de NTE
  #edgeListAdj = [(int(x)-1, int(y)-1) for x,y in edgeList]
  edgeListAdj = realEdgeList(numNodes, edgeList)
  nodeList = [i for i in range(numNodes)]
  voisinsDict = dict()
  for node in nodeList:
      voisinsDict[node] = []
      for elt0, elt1 in edgeListAdj:
        if elt0 == node and elt1 != node:    # ERROR: Key error: 0
          voisinsDict[node].append(elt1)
        if elt1 == node and elt0 != node:
          voisinsDict[node].append(elt0)

  Y = 0
  for node in NTE:
    relationship = False
    for voisin in voisinsDict[node]:
      if voisin in TE:
        relationship = True
    Y += int(relationship)
  answer = X - Y
  return answer

def coloration(numNodes, edgeList):
  #edgeListAdj = [(int(x)-1, int(y)-1) for x,y in edgeList]
  edgeListAdj = realEdgeList(numNodes, edgeList)
  nodeList = [i for i in range(numNodes)]

  voisinsDict = dict()
  for node in nodeList:
      voisinsDict[node] = []
      for elt0, elt1 in edgeListAdj:
        if elt0 == node and elt1 != node:    # ERROR: Key error: 0
          voisinsDict[node].append(elt1)
        if elt1 == node and elt0 != node:
          voisinsDict[node].append(elt0)

  degreDict = dict()
  for node in nodeList:
    degreDict[node] = len(voisinsDict[node])

  coloration = [0 for _ in range(len(nodeList))]
  currentColor = 1
  nonVisited = [node for node in nodeList]

  # Coloration du premier sommet, celui de plus haut degre
  highestDegre = -1
  nodeToColor = 0
  for node in nodeList:
    if degreDict[node] > highestDegre:
      highestDegre = degreDict[node]
      nodeToColor = node
  coloration[nodeToColor] = 1
  nonVisited.remove(nodeToColor)

  # Tant qu on a pas visite tous les sommets
  while len(nonVisited) > 0:
    # Choisir un sommet NON VISITE avec un DSAT maximum
    # En cas d egalite, prendre celui avec le degre maximum
    DSATList = []
    for node in nonVisited:
      DSATList.append((node, DSAT(node, voisinsDict[node], coloration)))
    DSATList = sorted(DSATList, key = func, reverse = True)
    highestDSAT = DSATList[0][1]
    potentialNodes = []
    i = 0
    while i < len(DSATList) and DSATList[i][1] == highestDSAT:
      potentialNodes.append(DSATList[i][0])
      i += 1
    # si highest_DSAT unique alors c'est le noeud a colorer
    if len(potentialNodes) == 1:
      nodeToColor = potentialNodes[0]
    else:
      highestDegre = -1
      nodeToColor = 0
      for node in potentialNodes:
        if degreDict[node] > highestDegre:
          highestDegre = degreDict[node]
          nodeToColor = node
    # Trouver la coloration minimale a ce noeud
    color = 1
    # faut la liste des couleurs des voisins
    voisinsColorList = []
    for node in voisinsDict[nodeToColor]:
      voisinsColorList.append(coloration[node])
    while color in voisinsColorList:
      color += 1
    coloration[nodeToColor] = color
    nonVisited.remove(nodeToColor)
  return coloration

def DSAT(sommet, voisinList, coloration):
  colors = []
  for voisin in voisinList:
    colors.append(coloration[voisin])
  return len(set(colors))

def func(x):
  return x[1]

def realEdgeList2(numNodes, edgeList):
  d = dict()
  counter = 0
  for elt0, elt1 in edgeList:
    if elt0 not in d:
      d[elt0] = counter
      counter += 1
    if elt1 not in d:
      d[elt1] = counter
      counter += 1
  newEdgeList = []
  for elt0, elt1 in edgeList:
    newEdgeList.append((d[elt0], d[elt1]))
  return newEdgeList

def realEdgeList(numNodes, edgeList):
  newList = []
  for edge in edgeList:
    newList.append((list(edge.values())[0] - 1, list(edge.values())[1] - 1))
  return newList

# peut avoir des pb: entre les nodes de nodeList et ceux de realEdgeList
# si on a: ValueError: too many values to unpack
# c est que edgeList est un dictionnaire...
#numnodes = 5
#edgelist = [{'edgeA': 1, 'edgeB': 2}, {'edgeA': 1, 'edgeB': 3}, {'edgeA': 1, 'edgeB': 4}, {'edgeA': 1, 'edgeB': 5}]
#edgelist = [{'edgeA': 1, 'edgeB': 3}, {'edgeA': 1, 'edgeB': 4}, {'edgeA': 1, 'edgeB': 5}, {'edgeA': 2, 'edgeB': 3}, {'edgeA': 2, 'edgeB': 4}, {'edgeA': 2, 'edgeB': 5}] 
#print(question03(numnodes, edgelist))
