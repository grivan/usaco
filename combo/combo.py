"""
ID: grivan.1
LANG: PYTHON3
TASK: combo
"""
fin = open ('combo.in', 'r')
fout = open ('combo.out', 'w')

N = int(fin.readline().split()[0])
a1, a2, a3 = map(int, fin.readline().split())
b1, b2, b3 = map(int, fin.readline().split())

count = 0
soln = []

sim = [(2, N), (1, N), (1, N-1),(N, 2), (N, 1), (N-1, 1)]

def compare(i, j, k, a, b, c):
 one, two, three = False, False, False
 if abs(i-a) < 3 or (i,a) in sim:
  one = True
 if abs(j-b) < 3 or (j,b) in sim:
  two = True
 if abs(k-c) < 3 or (k,c) in sim:
  three = True
 return one and two and three

def compare2(i, a, b):
 if abs(i-a) < 3 or (i, a) in sim:
  return 1
 elif abs(i-b) < 3 or (i, b) in sim:
  return 2
 return -1

for i in range(1, N+1):
 r1 = compare2(i,a1,b1)
 if r1 == -1: continue
 for j in range(1, N+1):
  r2 = compare2(j,a2,b2)
  if r2 == -1: continue
  for k in range(1, N+1):
   r3 = compare2(k,a3,b3)
   if r3 == -1: continue
   if compare(i,j,k,a1,a2,a3) or compare(i,j,k,b1,b2,b3):
    count+=1
    soln.append([i,j,k])

#r = 9
#for i in range(int(len(soln)/r)+1):
# sub = map(lambda x: ",".join([str(i) for i in x]), soln[i*r:(i+1)*r])
# print("\t".join(sub))

#print(count)
fout.write (str(count) + '\n')
fout.close()
