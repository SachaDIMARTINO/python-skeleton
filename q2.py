# ONLY EDIT FUNCTIONS MARKED CLEARLY FOR EDITING

import numpy as np

def question02(cashflow_in, cashflow_out):
  answer = -1
  answer = 0
  return answer

#compute all combinations for two portfolios
def question02bis(cashflow_in, cashflow_out):
  # modify and then return the variable below
  answer = -1
  if len(cashflow_in) == 0:
    answer = min(cashflow_out)
    return answer
  elif len(cashflow_out) == 0:
    answer = min(cashflow_in)
    return answer
  if len(cashflow_in) > len(cashflow_out):
    shortList = cashflow_out
    longList = cashflow_in
  else:
    shortList = cashflow_in
    longList = cashflow_out
  output = 0
  test = False
  powerSet = list(powerset(shortList))
  for subset in powerSet[1:]:
    if isSubsetSum(longList, len(longList), sum(subset) + output) or isSubsetSum(longList, len(longList), sum(subset) - output):
      test = True
  while test == False:
    output += 1
    for subset in powerSet[1:]:
      if isSubsetSum(longList, len(longList), sum(subset) + output) or isSubsetSum(longList, len(longList), sum(subset) - output):
        test = True
  answer = output
  answer = min(answer, min(cashflow_in), min(cashflow_out))
  return answer

def isSubsetSum (arr, n, summ): 
    # Base Cases 
    if summ == 0: 
        return True
    if n == 0 and summ != 0: 
        return False
  
    # If last element is greater than sum, then  
    # ignore it 
    if arr[n-1] > summ: 
        return isSubsetSum (arr, n-1, summ) 
  
    ''' else, check if sum can be obtained by any of  
    the following 
    (a) including the last element 
    (b) excluding the last element'''
      
    return isSubsetSum (arr, n-1, summ) or isSubsetSum (arr, n-1, summ-arr[n-1])

from itertools import chain, combinations
def powerset(iterable):
    """
    powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)
    """
    xs = list(iterable)
    # note we return an iterator rather than a list
    return chain.from_iterable(combinations(xs,n) for n in range(len(xs)+1))

# cin = [72], cout = [27] must return 27, not 45...
# cin = [72, 1], cout = [27] must return 1, not 26...
# a question has timed out
