class UnionFind:
    def __init__(self, total):
        self.parent = [i for i in range(total)]

    def find(self, e):
        if self.parent[e] != e:
            self.parent[e] = self.find(self.parent[e])
        return self.parent[e]

    def union(self, e1, e2):
        parent_1 = self.find(e1)
        parent_2 = self.find(e2)

        if parent_1 != parent_2:
            self.parent[parent_2] = parent_1

    def are_connected(self, e1, e2):
        parent_1 = self.find(e1)
        parent_2 = self.find(e2)

        return parent_1 == parent_2

while True:
    m, n = map(int, input().split())
    
    if m == 0 and n == 0: break

    edges = []
    for i in range(n):
        x, y, z = map(int, input().split())
        edges.append((z, x, y))

    edges = sorted(edges, reverse = True)

    union_find = UnionFind(m)
    spared_money = 0

    while edges:
        z, x, y = edges.pop()
        if not union_find.are_connected(x, y):
            union_find.union(x, y)
        else:
            spared_money += z

    print(spared_money)