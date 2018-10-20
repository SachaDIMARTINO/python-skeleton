# ONLY EDIT FUNCTIONS MARKED CLEARLY FOR EDITING

# import numpy as np

# modify this function, and create other functions below as you wish
def question01(portfolios):
  # modify and then return the variable below
  answer = -1
  if len(portfolios) < 2:
    return answer
  if len(portfolios) > 100 or max(portfolios) >= 2**16 or min(portfolios) < 0:
    return answer
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
