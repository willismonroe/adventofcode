import networkx as nx
from itertools import *

f = open('input.txt')
rows = [line.strip() for line in f]

nr,nc,c,d = len(rows),len(rows[0]),dict(),dict()
G = nx.generators.classic.grid_2d_graph(nr,nc)

for i in range(nr):
  for j in range(nc):
    if rows[i][j]=='#':
      G.remove_node((i,j))
    if rows[i][j].isdigit():
      c[int(rows[i][j])] = (i,j)

for i in range(8):
  for j in range(8):
    d[i,j]=d[j,i]= nx.shortest_path_length(G,c[i],c[j])

best = 10**100
for p in permutations(range(1,8)):
  l = [0] + list(p)
  t = sum(d[l[i+1],l[i]] for i in range(len(l)-1))
  best = min(t,best)
print(best)

best_2 = 10**100
for p in permutations(range(1,8)):
  l = [0] + list(p) + [0]
  t = sum(d[l[i+1],l[i]] for i in range(len(l)-1))
  best_2 = min(t,best_2)
print(best_2)