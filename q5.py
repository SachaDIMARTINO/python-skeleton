# ONLY EDIT FUNCTIONS MARKED CLEARLY FOR EDITING

import numpy as np

def question05(allowedAllocations, totalValue):
  # modify and then return the variable below
  answer = -1
  X = sorted(allowedAllocations, reverse = True)
  for i in range(len(X)):
    res = [X[i]]
    while sum(res) < totalValue and i < len(X):
      if X[i] > 0:
        if totalValue % X[i] == 0:
          if sum(res) + X[i] <= totalValue:
            res.append(X[i])
          else:
            i += 1
        elif sum(res) + X[i] <= totalValue:
          res.append(X[i])
        else:
          i += 1
      else:
        i += 1
    if sum(res) == totalValue and (len(res) < answer or answer < 0):
      answer = len(res)
  return answer

# ERROR: Timed out. test must be < 1 sec
# ERROR: 31/100 are incorrect. Then I changed answer = -1 instead of 20001
