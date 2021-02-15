a = [1,3,4]
for i in range(len(a)):
    if a[i]>2:
        a.insert(i,2)
        break
print(a)