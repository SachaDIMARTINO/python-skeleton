# ONLY EDIT FUNCTIONS MARKED CLEARLY FOR EDITING

import numpy as np

#compute all combinations for two portfolios
def question04(rows, numberMachines):
  # modify and then return the variable below
  answer = 20001
  for row in rows:
    # window
    for start in range(len(row) - numberMachines + 1):
      end = start + numberMachines
      shortRow = row[start:end]
      # si que des int dans shortRow
      if all(isinstance(x, int) for x in shortRow):
        if sum(shortRow) < answer:
          answer = sum(shortRow)
  if answer == 20001:
    answer = 0
  return answer
