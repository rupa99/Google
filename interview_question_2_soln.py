import sys

def solution(A):
  sys.stderr.write(
      'Tip: Use sys.stderr.write() to write debug messages on the output tab.\n'
  )
  hash_map = {}
  poss_sol = []
  sol_diff = float('inf')
  for k in A:
    hash_map[k] = hash_map.get(k, 0) + 1
  print(hash_map)



  for key in hash_map:
    if(hash_map[key] >= 2):
        poss_sol.append(key)
    if(hash_map[key] >= 4):
        return 0
  print(poss_sol)

  if(len(poss_sol) < 2):
    return -1

  for i in range(len(poss_sol)):
    
    for j in range(i+1, len(poss_sol)):
        varx = poss_sol[i]
        vary = poss_sol[j]
        res = abs(varx - vary)
        if(res < sol_diff):
            sol_diff = res
    
  return sol_diff

#input = [2,2,2,2,2]
#input = [911, 1, 3, 1000, 1000, 2, 2, 999, 1000, 911]
# input = [4, 1, 1, 1, 3]
input = [1, 1, 1]
print(solution(input))