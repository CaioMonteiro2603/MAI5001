def intersect(rect1, rect2):
    x1, y1, w1, h1 = rect1
    x2, y2, w2, h2 = rect2

    x_overlap = max(0, min(x1 + w1, x2 + w2) - max(x1, x2))
    y_overlap = max(0, min(y1 + h1, y2 + h2) - max(y1, y2))

    if x_overlap > 0 and y_overlap > 0:
        x_intersect = max(x1, x2)
        y_intersect = max(y1, y2)
        w_intersect = min(x1 + w1, x2 + w2) - x_intersect
        h_intersect = min(y1 + h1, y2 + h2) - y_intersect
        return True, (x_intersect, y_intersect, w_intersect, h_intersect)
    else:
        return False, None

# Primeira entrada
rect1_case1 = list(map(int, input().split()))
rect2_case1 = list(map(int, input().split()))

intersected, intersection_rect = intersect(rect1_case1, rect2_case1)

if intersected:
    x, y, w, h = intersection_rect
    print(f"HIT: {x} {y} {w} {h}")
else:
    print("MISS")

