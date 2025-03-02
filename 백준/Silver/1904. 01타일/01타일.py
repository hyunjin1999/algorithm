n = int(input())
if n ==1 or n == 2:
    print(n)
    exit()
a = []

for i in range(n):
    a.append(0)
a[0],a[1] = 1,2
for i in range(2, n):
    a[i] = (a[i-1] + a[i-2])%15746

print(a[-1])