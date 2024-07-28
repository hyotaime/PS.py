def selection_sort(arr, k):
    cnt = 0
    for i in range(len(arr) - 1, 0, -1):
        max_index = 0
        for j in range(i + 1):
            if arr[j] > arr[max_index]:
                max_index = j
        if max_index != i:
            cnt += 1
            arr[i], arr[max_index] = arr[max_index], arr[i]
            if cnt == k:
                print(arr[max_index], arr[i])
                return True
    return False


if __name__ == '__main__':
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    if not selection_sort(arr, k):
        print(-1)
