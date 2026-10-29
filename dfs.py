#function to peform DFS

def dfs(graph,node,visited):
    if node not in visited:
        print(node, end=" ")
        visited.add(node)

        for neighbor in graph[node]:
            dfs(graph,neighbor,visited)

#Main program
graph={}
n=int(input("Enter the no. of vertices: "))
for i in range(n):
    vertex=input(f"Enter vertex{i+1}: ")
    neighbors=input(f"Enter adjacent vertices of {vertex} (space-separated): ").split()
    graph[vertex]=neighbors

start=input("Enter the statng vertex: ")
print("\nGraph: ",graph)
print("DFS Traversal: ",end=" ")
visited=set()
dfs=(graph,start,visited)
#function to peform DFS

def dfs(graph,node,visited):
    if node not in visited:
        print(node, end=" ")
        visited.add(node)

        for neighbor in graph[node]:
            dfs(graph,neighbor,visited)

#Main program
graph={}
n=int(input("Enter the no. of vertices: "))
for i in range(n):
    vertex=input(f"Enter vertex{i+1}: ")
    neighbors=input(f"Enter adjacent vertices of {vertex} (space-separated): ").split()
    graph[vertex]=neighbors

start=input("Enter the statng vertex: ")
print("\nGraph: ",graph)
print("DFS Traversal: ",end=" ")
visited=set()
dfs(graph,start,visited)

#output
# Enter the no. of vertices: 4
# Enter vertex1: A
# Enter adjacent vertices of A (space-separated): B C
# Enter vertex2: B
# Enter adjacent vertices of B (space-separated): A D
# Enter vertex3: C
# Enter adjacent vertices of C (space-separated): A
# Enter vertex4: D
# Enter adjacent vertices of D (space-separated): B
# Enter the statng vertex: A
# 
# Graph:  {'A': ['B', 'C'], 'B': ['A', 'D'], 'C': ['A'], 'D': ['B']}
# DFS Traversal:  A B D C 