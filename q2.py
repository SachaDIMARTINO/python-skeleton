# ONLY EDIT FUNCTIONS MARKED CLEARLY FOR EDITING

import numpy as np

#compute all combinations for two portfolios
def question02(cashflow_in, cashflow_out):
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
  return answer

