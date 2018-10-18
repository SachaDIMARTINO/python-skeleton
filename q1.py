# ONLY EDIT FUNCTIONS MARKED CLEARLY FOR EDITING

#import numpy as np

# modify this function, and create other functions below as you wish
def question01(portfolios):
  # modify and then return the variable below
  answer = -1
  for i in range(len(portfolios)-1):
    for j in range(i+1, len(portfolios)):
      X1 = bitfield(portfolios[i])
      X2 = bitfield(portfolios[j])
      C = [X1[k] ^ X2[k] for k in range(16)]
      answer = max(answer, intfield(C))
  return answer

def bitfield(n):
  X = [1 if digit=='1' else 0 for digit in bin(n)[2:]]
  Y = [0 for _ in range(16-len(X))]
  return Y + X

def intfield(L):
  counter = 0
  for i in range(16):
    counter += L[15-i] * 2**i
  return counter
