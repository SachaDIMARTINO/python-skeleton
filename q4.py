# ONLY EDIT FUNCTIONS MARKED CLEARLY FOR EDITING

import numpy as np

#compute all combinations for two portfolios
def question04(rows, numberMachines):
  # modify and then return the variable below
  # generic cases
  if len(rows) == 0 or numberMachines <= 0:
    answer = 0
    return answer
  # constraints
  if numberMachines > 100 or len(rows) > 100:
    answer = 0
    return answer
  arrInt = [[elt if type(elt) == int else 0 for elt in arr[i]] for i in range(len(arr))]
  infinity = max(map(max, arrInt))
  answer = infinity
  for row in rows:
    # window
    for start in range(len(row) - numberMachines + 1):
      end = start + numberMachines
      shortRow = row[start:end]
      print(row, start, end, shortRow)
      # si que des int dans shortRow
      if all(isinstance(x, int) for x in shortRow):
        answer = min(answer, sum(shortRow))
  if answer == infinity:
    answer = 0
  return answer
