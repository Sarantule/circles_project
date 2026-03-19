import math


def radius_sum(r1, r2):
    return r1 + r2


def has_intersection(x1, y1, r1, x2, y2, r2):
    distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

    if distance > r1 + r2:
        return False

    if distance < abs(r1 - r2):
        return False

    return True