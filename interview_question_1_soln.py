import sys


def solution(S):
  sys.stderr.write(
      'Tip: Use sys.stderr.write() to write debug messages on the output tab.\n'
  )

  pattern = ['a', 'b', 'c']
  insert = 0
  index = 0
  x = 0

  while x != ((len(S))):
    curr = S[x]
    patt = pattern[index]
    if(curr != patt):
        insert = insert + 1
        index = index + 1
        #print(patt)

        if(index == 3):
            index = 0
        continue

    else:
        #print(curr)
        index = index + 1
        if(index == 3):
            index = 0
        x = x + 1

      
  return insert

#S= "aabcc"
#S = "abcabcabca"
S = "bcaaa"
final = solution(S)

print(final)