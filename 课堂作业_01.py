#生成斐波那契数列并筛选其中的元素
#例如[0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
a = [0,1]
for i in range(1,11):
    a.append(a[i]+a[i-1])
print(a)
for n in range(len(a)):
    if a[n]>10:
        print(a[n])
