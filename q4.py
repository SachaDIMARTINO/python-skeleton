# ONLY EDIT FUNCTIONS MARKED CLEARLY FOR EDITING

"""
def question04(rows, numberMachines):
  # modify and then return the variable below
  # constraints and generic cases
  if len(rows) == 0 or numberMachines <= 0 or numberMachines > 100 or len(rows) > 100 or len(rows[0]) == 0:
    answer = 0
    return answer
  arrInt = [[elt if type(elt) == int else 0 for elt in rows[i]] for i in range(len(rows))]
  infinity = numberMachines * (max(map(max, arrInt)) + 1)
  answer = infinity
  for row in rows:
    # window
    for start in range(len(row) - numberMachines + 1):
      end = start + numberMachines
      shortRow = row[start:end]
      # si que des int dans shortRow
      if all(isinstance(x, int) for x in shortRow):
        answer = min(answer, sum(shortRow))
  if answer == infinity:
    answer = 0
  return answer
"""
def question04(rows, numberMachines):
  # modify and then return the variable below
  # constraints and generic cases
  if len(rows) == 0 or numberMachines <= 0 or numberMachines > 100 or len(rows) > 100 or len(rows[0]) == 0:
    answer = 0
    return answer
  arrInt = [[elt if type(elt) == int else 0 for elt in rows[i]] for i in range(len(rows))]
  infinity = numberMachines * (max(map(max, arrInt)) + 1)
  answer = infinity
  for row in rows:
    rowInt = [elt for elt in row if type(elt) == int]
    # window
    for start in range(len(rowInt) - numberMachines + 1):
      end = start + numberMachines
      shortRow = rowInt[start:end]
      answer = min(answer, sum(shortRow))
  if answer == infinity:
    answer = 0
  return answer

# WARNING: rows = np.array([18, 'X', 19]) --> list(rows)[0][0] is '18' a np.str
