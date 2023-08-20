class Node:
    def _init_(self, data):
        self.data = data
        self.left = self.right = None


def OBST(r, i, j):
    k = r[i][j]
    if k != 0:
        node = Node(a[k-1])
        node.left = OBST(r, i, k-1)
        node.right = OBST(r, k, j)
        return node


def Preorder(root):
    if root:
        print(root.data, end=" ")
        Preorder(root.left)
        Preorder(root.right)


def table(p, q, n):
    m = [[0]*(n+1) for _ in range(n+1)]
    c = [[0]*(n+1) for _ in range(n+1)]
    r = [[0]*(n+1) for _ in range(n+1)]
    for l in range(0, n+1):
        for i in range(0, n+1-l):
            j = i+l
            if i == j:
                m[i][j] = q[j]
            else:
                m[i][j] = p[j] + q[j] + m[i][j-1]
                c[i][j] = float('inf')
                for k in range(i+1, j+1):
                    sol = c[i][k-1] + c[k][j] + m[i][j]
                    if sol < c[i][j]:
                        c[i][j] = sol
                        r[i][j] = k
    Tree = OBST(r, 0, 4)
    print("Preorder Traversal:", end=" ")
    Preorder(Tree)


if __name__ == "__main__":
    a = [x for x in input("Enter the identifier sets: ").split()]
    p = [int(x) for x in input("Enter successful trails i.e. p(1:n): ").split()]
    p.insert(0, 0)
    q = [int(x) for x in input("Enter successful trails i.e. q(0:n): ").split()]
    q.insert(0,0)
    table(p, q, len(a))