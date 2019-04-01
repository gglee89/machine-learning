def Merge(B, C, A):
    i = j = k = 0
    p = len(B)
    q = len(C)

    while i < p and j < q:
        if B[i] <= C[j]:
            A[k] = B[i]
            i = i + 1
        else:
            A[k] = C[j]
            j = j + 1

        k = k + 1

    if i == p:
        A[k:p+q] = C[j:q]
    else:
        A[k:p+q] = B[i:p]


def Sort(numbers):
    lower_half = []
    upper_half = []
    if len(numbers) > 1:
        size = len(numbers)
        lower_half = numbers[0:size/2]
        upper_half = numbers[size/2:size]
        Sort(lower_half)
        Sort(upper_half)
        Merge(lower_half, upper_half, numbers)
        return numbers


numbers = [4, 6, 2, 3, 4, 1, 8, 6, 9, 20]
print('Numbers: [' + ','.join([str(number) for number in numbers]) + ']')

numbers_sorted = Sort(numbers)
print('Numbers Sorted: [' + ','.join([str(number)
                                      for number in numbers_sorted]) + ']')

minimum, maximum = numbers_sorted[0], numbers_sorted[len(numbers_sorted) - 1]
print('Minimum: ' + str(minimum))
print('Maximum: ' + str(maximum))
