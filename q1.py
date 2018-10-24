# ONLY EDIT FUNCTIONS MARKED CLEARLY FOR EDITING

# modify this function, and create other functions below as you wish
def question01(portfolios):
  # modify and then return the variable below
  answer = 0
  if len(portfolios) < 2 or max(portfolios) == 0:
    return answer
  answer = max([portfolios[i] ^ portfolios[j] for i in range(len(portfolios)-1) for j in range(i+1, len(portfolios))])
  return answer
