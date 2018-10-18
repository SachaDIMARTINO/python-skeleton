# ONLY EDIT FUNCTIONS MARKED CLEARLY FOR EDITING

#import numpy as np

def question03(numNodes, edgeList):
  # modify and then return the variable below
  answer = -1
  return answer
  for edge in edgeList:
    source = edge[0] # IT SHOULD WORK
    destination = edge[1] # IT SHOULD WORK
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
  edgeListAdj = []
  for i in range(len(edgeList)):
    edgeListAdj.append((int(list(edgeList[i])[0]) - 1, int(list(edgeList[i])[1]) - 1)) #IS IT WORKING
  nodeList = [i for i in range(numNodes)]
  voisinsDict = dict()
  for node in nodeList:
      voisinsDict[node] = []
      for elt in edgeListAdj:
        if elt[0] == node and elt[1] != node:    # ERROR: Key error: 0
          voisinsDict[node].append(elt[1])
        if elt[1] == node and elt[0] != node:
          voisinsDict[node].append(elt[0])

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
  edgeListAdj = []
  for edge in edgeList:
    sourceDestination = []
    for elt in edge:
      if type(elt) == int:
        sourceDestination.append(elt)
    source = sourceDestination[0]
    destination = sourceDestination[1]
    edgeListAdj.append((source - 1, destination - 1)) # is it working v2
  nodeList = [i for i in range(numNodes)]

  voisinsDict = dict()
  for node in nodeList:
      voisinsDict[node] = []
      for elt in edgeListAdj:
        if elt[0] == node and elt[1] != node:    # ERROR: Key error: 0
          voisinsDict[node].append(elt[1])
        if elt[1] == node and elt[0] != node:
          voisinsDict[node].append(elt[0])

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
