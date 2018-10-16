# ONLY EDIT FUNCTIONS MARKED CLEARLY FOR EDITING

import numpy as np

# modify this function, and create other functions below as you wish
def question01(portfolios):
  # modify and then return the variable below
  answer = 0
  for i in range(len(portfolios)):
    for j in range(i+1, len(portfolios)):
      if merge_portfolios(portfolios[i], portfolios[j]) > answer:
        answer = merge_portfolios(portfolios[i], portfolios[j])
  return answer

def bitfield(n):
    X = [1 if digit=='1' else 0 for digit in bin(n)[2:]]
    Y = [0 for _ in range(16-len(X))]
    return Y + X

def merge_portfolios(p1, p2):
  X2 = bitfield(p2)
  C = bitfield(p1)
  for i in range(16):
    if C[i] + X2[i] == 2:
      C[i] = 0
    elif X2[i] == 1 and C[i] == 0:
      C[i] = 1
  counter = 0
  for i in range(len(C)):
    counter += C[i] * 2 ** (16-i-1)
  return counter

# HOW TO AVOID THE 2 FOR LOOPS... ?
