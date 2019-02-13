if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    arr = list(arr)
    first = max(arr)
    runner_up = max([x for x in arr if x != first])
    print(runner_up)
