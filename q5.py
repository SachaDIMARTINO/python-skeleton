# ONLY EDIT FUNCTIONS MARKED CLEARLY FOR EDITING

import numpy as np

def question05(allowedAllocations, totalValue):
  # modify and then return the variable below
  answer = 20001
  X = sorted(allowedAllocations, reverse = True)
  for i in range(len(X)):
    res = [X[i]]
    while sum(res) < totalValue and i < len(X):
      if totalValue % X[i] == 0:
        if sum(res) + X[i] <= totalValue:
          res.append(X[i])
        else:
          i += 1
      elif sum(res) + X[i] <= totalValue:
        res.append(X[i])
      else:
        i += 1
    if sum(res) == totalValue and len(res) < answer:
      answer = len(res)
      #tmp = res
  #print(tmp)
  return answer
