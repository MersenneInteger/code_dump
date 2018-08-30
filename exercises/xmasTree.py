upperBound = int(input())
tree = [(' ' * ((upperBound - i) // 2), '*' * i) for i in range(1, upperBound, 2)]
for i in range(len(tree)):
    print(tree[i][0], tree[i][1])