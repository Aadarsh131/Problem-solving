# https://www.geeksforgeeks.org/problems/count-digits5716/1

#TOPICS- Modular Algorithm

def evenlyDivides (N):
  count = 0
  originalN = N
  while(N > 0):
      temp = N % 10
      N = N // 10
      if(temp == 0):
          continue
      if(originalN%temp == 0):
          count += 1
  return count

print(evenlyDivides(12))
