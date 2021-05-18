"""
ID: grivan.1
LANG: PYTHON3
TASK: skidesign
"""
fin = open ('skidesign.in', 'r')
fout = open ('skidesign.out', 'w')

N = int(fin.readline().split()[0])
hills = []
for i in range(N):
 hills.append(int(fin.readline()))

hills = sorted(hills)

intervals = []
for i in range(100 - 17 + 1):
  intervals.append((i,i+17))

costs = []
for int in intervals:
  low, hi = int[0], int[1]
  cost = 0
  for hill in hills:
    if hill < low:
      cost += (low - hill)**2
    elif hill > hi:
      cost += (hill - hi)**2
  costs.append(cost)

amount = min(costs)
fout.write(str(amount) + '\n')
fout.close()
