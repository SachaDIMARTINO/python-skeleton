# ONLY EDIT FUNCTIONS MARKED CLEARLY FOR EDITING

import numpy as np

# modify this function, and create other functions below as you wish
def question01(portfolios):
  # modify and then return the variable below
  answer = -1
  if len(portfolios) == 0:
    answer = 0
    return answer
  if len(portfolios) > 100 or max(portfolios) >= 2**16:
    return answer
  for i in range(len(portfolios)-1):
    for j in range(i+1, len(portfolios)):
      X1 = bitfield(portfolios[i])
      X2 = bitfield(portfolios[j])
      C = [X1[k] ^ X2[k] for k in range(16)]
      answer = max(answer, C.count(1))
  return answer

def bitfield(n):
  X = [1 if digit=='1' else 0 for digit in bin(n)[2:]]
  Y = [0 for m in range(16-len(X))]
  return Y + X

def intfield(L):
  counter = 0
  for l in range(16):
    counter += L[15-l] * 2**l
  return counter
