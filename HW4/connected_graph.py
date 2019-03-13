def Connected(matrix):
    length = len(matrix)

    if (length == 1):
        return 1
    else:
        if not Connected([initialMatrix[i][0:length-1] for i in range(0, length-1)]):
            return 0
        else:
            for j in range(length-1):
                if matrix[length-1][j]:
                    return 1
            return 0

initialMatrix = [
    [0, 1, 1, 0],
    [1, 0, 1, 1],
    [1, 1, 0, 1],
    [0, 1, 1, 0]
]
result = Connected(initialMatrix)

print("Graph is " + 'Connected' if result == 1 else 'Not Connected')
