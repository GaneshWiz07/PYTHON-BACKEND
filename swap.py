arr=[57,38,91,10,38,28,79,41]
swap=0
for i in range(len(arr)):
    for j in range(i+1,len(arr)):
        if arr[i]==arr[j]:
            continue
        elif arr[i]>arr[j]:
            arr[i],arr[j]=arr[j],arr[i]
            swap+=1

print("SORTED ARRAY:",arr)
print("SWAP COUNT:",swap)
