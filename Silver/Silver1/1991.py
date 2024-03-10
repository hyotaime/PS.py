import sys

input = sys.stdin.readline


def preorder(node):
    if node == -19:
        return
    print(chr(node + 65), end='')
    preorder(graph[node][0])
    preorder(graph[node][1])


def inorder(node):
    if node == -19:
        return
    inorder(graph[node][0])
    print(chr(node + 65), end='')
    inorder(graph[node][1])


def postorder(node):
    if node == -19:
        return
    postorder(graph[node][0])
    postorder(graph[node][1])
    print(chr(node + 65), end='')


if __name__ == '__main__':
    n = int(input())
    graph = [[0, 0] for _ in range(n)]
    for _ in range(n):
        root, left, right = input().split()
        graph[ord(root) - 65] = [ord(left) - 65, ord(right) - 65]
    preorder(0)
    print()
    inorder(0)
    print()
    postorder(0)
    print()
