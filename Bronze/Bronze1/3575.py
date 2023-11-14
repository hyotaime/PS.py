import sys

input = sys.stdin.readline
s1 = input().rstrip()
s2 = input().rstrip()
t1 = input().rstrip()
t2 = input().rstrip()
dict = {}


def build(s1, s2):
    s2 = s2[::-1]
    result = [s1[i] + s2[i] for i in range(len(s1))]
    result.sort()
    return result


print("Yes" if build(s1, s2) == build(t1, t2) else "No")
