A = [22, 25, 21, 23, 20, 24]
for i in range(len(A)) :
    min_idx = i
    for j in range(i+1, len(A)) :
        if A[min_idx] > A[j] :
            min_idx = j

    A[i], A[min_idx] = A[min_idx], A[i]

print ("Sorted array is : ")
for i in range(len(A)) :
    print("%d" %A[i]),
