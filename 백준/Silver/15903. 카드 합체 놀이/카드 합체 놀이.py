n, m = map(int, input().split())
cards = list(map(int, input().split()))

for _ in range(m):
    cards.sort()
    min1 = cards[0]
    min2 = cards[1]
    cards[0], cards[1] = min1 + min2, min1 + min2

print(sum(cards))