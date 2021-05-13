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
# print("x_max = "+str(x_max))
# print("a=(0,0) b=(1,0) c=(1,1) d=(0,1)")

# you have to go into a wormhole to get into a loop
# so we start with each wormhole and then see if we get
# stuck in a loop (arrive at the same wormhole again)
def check(pairs):
  loop = False
  for hole in wholes:
    current = hole
    seen = set()
    seen.add(current)
    while(not loop and current[0] <= x_max):
      if current in pairs:
        current = pairs[current]
        current = (current[0] + 1, current[1])
      else:
        current = (current[0] + 1, current[1])
      if current in seen:
        # print("deteced!")
        loop = True
        break
      else:
         seen.add(current)
    if loop: return 1
  return 0

total = 0
def generate(wholes, pairs):
  global total
  if len(wholes) == 0:
    if check(pairs):
      # print("loop :" + str(pairs))
      total+=1
    return

  hole1 = wholes.pop()
  for hole in wholes:
    pairs[hole] = hole1
    pairs[hole1] = hole
    nwholes = wholes.copy()
    nwholes.remove(hole)
    generate(nwholes, pairs)
    del pairs[hole]
    del pairs[hole1]

generate(wholes.copy(), dict())
# print("check = " + str(check({(1, 0): (0, 1), (0, 0): (1, 1)})))
# print(total)
fout.write(str(total) + '\n')
fout.close()
