# pypy
def closest_pair(S):
    n = len(S)

    # 3개 이하일 경우 그냥 단순 계산
    if n <= 3:
        m = float('inf')
        for i in range(n):
            for j in range(i + 1, n):
                d = (S[i][0] - S[j][0]) ** 2 + (S[i][1] - S[j][1]) ** 2
                m = min(m, d)
        return m

    # x좌표를 기준으로 정렬
    S.sort(key=lambda point: point[0])

    # 가운데 인덱스
    mid = n // 2

    # 배열 나누기
    S_left = S[:mid]
    S_right = S[mid:]

    # 분할한 부분의 최소 거리 계산
    m_left = closest_pair(S_left)
    m_right = closest_pair(S_right)

    # 두 부분중 최소값을 m에 저장
    m = min(m_left, m_right)

    # 가운데 부분의 최소 거리 계산
    strip = []
    for point in S:
        if (point[0] - S[mid][0]) ** 2 < m:
            strip.append(point)

    # 중간 영역에서의 최소 거리 계산
    m_mid = closest_strip(strip, m)

    # 최소 거리 중 최솟값 반환
    return min(m, m_mid)


def closest_strip(strip, m):
    # y좌표를 기준으로 정렬
    strip.sort(key=lambda point: point[1])

    # 중복되는 점을 피하기 위해 미리 계산한 최소 거리를 사용
    for i in range(len(strip)):
        j = i + 1
        while j < len(strip) and (strip[j][1] - strip[i][1]) < m:
            d = (strip[i][0] - strip[j][0]) ** 2 + (strip[i][1] - strip[j][1]) ** 2
            m = min(m, d)
            j += 1

    return m


# 입력
n = int(input())
points = []

for _ in range(n):
    x, y = map(int, input().split())
    points.append((x, y))

# 결과 출력
print(closest_pair(points))
