# ONLY EDIT FUNCTIONS MARKED CLEARLY FOR EDITING

import numpy as np

# modify this function, and create other functions below as you wish
def question01(portfolios):
  # modify and then return the variable below
  portfolios = list(portfolios)
  answer = -1
  if len(portfolios) == 0:
    answer = 0
    return answer
  if len(portfolios) == 1:
    answer = portfolios[0]
    return answer
  if max(portfolios) == 0:
    answer = 0
    return answer

  maxElt = max(portfolios)
  bitFort = sum([1 if maxElt-2**i >= 0 else 0 for i in range(16)]) - 1
  maxList = [elt for elt in portfolios if elt >= 2**bitFort]
  minList = [elt for elt in portfolios if elt not in maxList]
  # if portfolios = [15,15,15] or [15,16,17]
  if len(minList) == 0:
    minList = maxList
  for i in maxList:
    for j in minList:
      answer = max(answer, i ^ j)
  return answer


"""
# modify this function, and create other functions below as you wish
def question01(portfolios):
  # modify and then return the variable below
  portfolios = list(portfolios)
  answer = -1
  if len(portfolios) == 0:
    answer = 0
    return answer
  if len(portfolios) == 1:
    answer = portfolios[0]
    return answer
  if len(portfolios) > 100 or max(portfolios) >= 2**16:
    answer = 0
    return answer
  for i in range(len(portfolios)):
    portfolios[i] = abs(portfolios[i])
  tri = sorted(portfolios, reverse = True)
  maxElt = tri[0]
  maxList = []
  minList = []
  try:
      indBitFort = bitfield(maxElt).index(1)
  # que des 0 dans bitfield(maxElt) --> que des 0 dans portfolios --> return 0
  except:
      answer = 0
      return answer
  for elt in tri:
      if 1 in bitfield(elt) and bitfield(elt).index(1) == indBitFort:
          maxList.append(elt)
      else:
          minList.append(elt)
  for n1 in maxList:
      for n2 in minList:
          X1 = bitfield(n1)
          X2 = bitfield(n2)
          C = [X1[k] ^ X2[k] for k in range(16)]
          answer = max(answer, intfield(C))
  return answer

# bitfield(15) = [0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1]
def bitfield(n):
  X = [1 if digit=='1' else 0 for digit in bin(n)[2:]]
  Y = [0 for m in range(16-len(X))]
  return Y + X

# intfield([0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1]) = 15
def intfield(L):
  counter = 0
  for l in range(16):
    counter += L[15-l] * 2**l
  return counter
"""
