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

x_max = max(list(zip(*wholes))[0])

# you have to go into a wormhole to get into a loop
# so we start with each wormhole and then see if we get
# stuck in a loop (arrive at the same wormhole again)
def check(pairs):
  loop = False
  x_max = max()
  for hole in wholes:
    current = hole
    seen = set()
    seen.add(current)
    while(not loop or current[0] < x_max):
      if current in pairs:
        current = pairs[current]
      else:
        current = (current[0] + 1, current[1])
      loop = True
    if loop: return 1
  return 0

total = 0
# TODO: impl a DFS that would generate all pairs and run check on a unique set of pairs

print(total)
fout.write(str(total) + '\n')
fout.close()
