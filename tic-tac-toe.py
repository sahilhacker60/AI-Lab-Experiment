
# Function to perform DFS
def dfs(graph, node, visited):
    if node not in visited:
        print(node, end=" ")
        visited.add(node)

        for neighbor in graph[node]:
            dfs(graph, neighbor, visited)


# Main program
graph = {}

n = int(input("Enter the no. of vertices: "))

for i in range(n):
    vertex = input(f"Enter vertex {i+1}: ")
    neighbors = input(
        f"Enter adjacent vertices of {vertex} (space-separated): "
    ).split()
    graph[vertex] = neighbors

start = input("Enter the starting vertex: ")

print("\nGraph:", graph)
print("DFS Traversal:", end=" ")

visited = set()
dfs(graph, start, visited)

print()
#output
#Enter the no. of vertices: 4
#Enter vertex 1: A
#Enter adjacent vertices of A (space-separated): B C
#Enter vertex 2: B
#Enter adjacent vertices of B (space-separated): A D
#Enter vertex 3: C
#Enter adjacent vertices of C (space-separated): A
#Enter vertex 4: D
#Enter adjacent vertices of D (space-separated): B
#Enter the starting vertex: A

#Graph: {'A': ['B', 'C'], 'B': ['A', 'D'], 'C': ['A'], 'D': ['B']}
#DFS Traversal: A B D C