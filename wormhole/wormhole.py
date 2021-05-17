"""
ID: grivan.1
LANG: PYTHON3
TASK: wormhole
"""
fin = open('wormhole.in', 'r')
fout = open('wormhole.out', 'w')

N = int(fin.readline().split()[0])

wholes = []
for i in range(N):
  x,y = map(int, fin.readline().split())
  wholes.append((x,y))

partners = [-1 for i in range(N)]

# nright contains the nearest right for each hole
nright = [-1 for i in range(N)]
for i in range(N):
  for j in range(N):
    xi, yi = wholes[i]
    xj, yj = wholes[j]
    if xj > xi and yi == yj:
      if nright[i] == -1 or (xj - xi < wholes[nright[i]][0] - xi):
        nright[i] = j

def check():
  # print("partners = "+ str(partners))
  # print("nright = " + str(nright))
  for i in range(N):
    current = i
    # print("current = "+ str(current))
    for _ in range(N):
      current = nright[partners[current]]
      #print("with move "+ str(_) + " current = "+ str(current))
      if current == -1:
        break
    if current != -1:
      #print("loop! current = " + str(current))
      return 1
  return 0

def solve():
  total = 0
  ui = None
  for i in range(N):
    if partners[i] == -1:
      ui = i
      break
  else:
    # if every hole is paried
    if check(): return 1
    return 0
    
  for j in range(ui+1, N):
    if partners[j] == -1:
      partners[i] = j
      partners[j] = i
      total += solve()
      partners[i] = -1
      partners[j] = -1
  
  return total

# print(nright)
# print(wholes)
total = solve()

fout.write(str(total) + '\n')
fout.close()
