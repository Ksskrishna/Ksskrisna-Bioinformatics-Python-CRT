campus = {
    "Canteen": ["Admin Block", "Hostel"],
    "Auditorium": ["Library"],
    "Main Gate": ["Admin Block"],
    "Admin Block": ["Main Gate", "Library", "Canteen", "Engineering Block"],
    "Library": ["Admin Block", "Auditorium"],
    "Engineering Block": ["Admin Block", "Science Block"],
    "Science Block": ["Engineering Block"],
    "Hostel": ["Canteen"]
}

def bfs(start, target):
    visited = set()
    queue = [start]
    while queue:
        b = queue.pop(0)
        if b == target:
            return True
        if b not in visited: 
            visited.add(b)
            queue += [n for n in campus[b] if n not in visited]
    return False  # <-- moved outside the loop

def dfs(start, visited=None):
    if visited is None:
        visited = set()
    if start in visited:
        return
    print(start, end=' ')
    visited.add(start)
    for neighbor in campus[start]: 
        dfs(neighbor, visited)

def disconnected():
    visited = set()
    dfs(next(iter(campus)), visited)
    return set(campus.keys()) - visited

# adjacency list
print("1. Campus Map:")
for b, n in campus.items():
    print(f"{b} -> {', '.join(n)}")
print("\n2. path from library to auditorium exists: ")
print("Yes" if bfs("Library", "Auditorium") else "No")
print("\n3. Direct connections from admin block: ")
print(campus["Admin Block"])
print("\n4. DFS from main gate: ")
dfs("Main Gate")
print()
print("\n5. Disconnected Buildings: ")
d = disconnected()
print(d if d else "None, campus is fully connected")