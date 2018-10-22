# ONLY EDIT FUNCTIONS MARKED CLEARLY FOR EDITING

#import numpy as np

"""
# modify this function, and create other functions below as you wish
def question01(portfolios):
  # modify and then return the variable below
  portfolios = list(portfolios)
  answer = -1
  if len(portfolios) < 2 or max(portfolios) == 0:
    answer = 0
    return answer
  #[[i ^ j for j in range(i+1, len(portfolios))] for i in range(len(portfolios)-1)]
  answer = max([portfolios[i] ^ portfolios[j] for i in range(len(portfolios)-1) for j in range(i+1, len(portfolios))])
  return answer
"""

def question01(portfolios):
  # modify and then return the variable below
  portfolios = list(portfolios)
  answer = -1
  if len(portfolios) < 2 or max(portfolios) == 0:
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
