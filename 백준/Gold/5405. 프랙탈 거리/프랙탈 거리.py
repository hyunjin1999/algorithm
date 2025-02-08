import sys
import math

def hilbert_curve_to_xy(n, d):
    x, y = 0, 0
    s = 1
    while s < (1 << n):
        rx = (d & 2) >> 1
        ry = (d ^ rx) & 1
        
        if ry == 0:
            if rx == 1:
                x = s - 1 - x
                y = s - 1 - y
            x, y = y, x
        
        x += s * rx
        y += s * ry
        d //= 4
        s *= 2
    return x, y

def calculate_distance(n, h, o):
    x1, y1 = hilbert_curve_to_xy(n, h - 1)
    x2, y2 = hilbert_curve_to_xy(n, o - 1)
    distance = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2) * 10
    return round(distance)

def main():
    t = int(sys.stdin.readline().strip())
    results = []
    for _ in range(t):
        n, h, o = map(int, sys.stdin.readline().split())
        results.append(str(calculate_distance(n, h, o)))
    
    print("\n".join(results))

if __name__ == "__main__":
    main()