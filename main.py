from src.geometry import has_intersection

x1, y1, r1 = 0, 0, 5
x2, y2, r2 = 6, 0, 5

result = has_intersection(x1, y1, r1, x2, y2, r2)

if result:
    print("Kružnice se protínají.")
else:
    print("Kružnice se neprotínají.")