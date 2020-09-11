v = [None for i in range(9)]
p = [None for i in range(9)]
q = [0]
a = [[1,3,8],[0,7],[3,5,7],[0,2,4],[3,8],[2,6],[5],[1,2],[0,4]]
def BFS(a):#Here 'a' is a graph in adjacency list form
	if len(q)==0:
		return
	i = q[0]
	del q[0]
	for j in range(len(a[i])):
		if v[a[i][j]]==None:
			v[a[i][j]] = 1
			q.append(a[i][j])
			p[a[i][j]] = i
	BFS(a)
def path(n):#returns an array which is the shortest path of node 'n' from root(usually '0'if q in above case is passed as [0])
	a = []
	while n!=0:
		a.append(n)
		n = p[n]
	a.append(0)
	return a

BFS(a)
k = path(6)
print(len(k)-1)

