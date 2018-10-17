# ONLY EDIT FUNCTIONS MARKED CLEARLY FOR EDITING

import numpy as np

# modify this function, and create other functions below as you wish
def question01(portfolios):
  # modify and then return the variable below
  answer = -1
  for i in range(len(portfolios)):
    for j in range(i+1, len(portfolios)):
      tmp = merge_portfolios(portfolios[i], portfolios[j])
      if tmp > answer:
        answer = tmp
  return answer

def bitfield(n):
  X = [1 if digit=='1' else 0 for digit in bin(n)[2:]]
  Y = [0 for _ in range(16-len(X))]
  return Y + X

def merge_portfolios(p1, p2):
  X2 = bitfield(p2)
  C = bitfield(p1)
  for i in range(16):
    C[i] = (C[i] + X2[i]) % 2
  counter = 0
  for j in range(len(C)):
    counter += C[j] * 2 ** (15-j)
  return counter
