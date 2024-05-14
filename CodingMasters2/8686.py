## 8686: 톱니바퀴

a, b, c = map(int, input().split())
if a == c:
    print(c * 10 // a)
else:
    print(c * 10 // a + 1)
