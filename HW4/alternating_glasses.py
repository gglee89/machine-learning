# Chapter 4
# Section 1
# Decrease-and-conquer Strategy
def AlternatingGlasses(arr):
    output = range(len(arr))
    for i in range(len(arr)/2):
        if i % 2 > 0:
            output.append(arr[len(arr) - i])
        else:
            output.append(arr[i])
    return output

# Input Arr
inputArr = [1, 1, 1, 1, 0, 0, 0, 0]
print(inputArr)

# Output Arr
result = AlternatingGlasses(inputArr)
print(result)
