import math
import matplotlib.pyplot as plt

# 5 test cases
def has_intersection(x1, y1, r1, x2, y2, r2):
    distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    if distance > r1 + r2:
        return False
    if distance < abs(r1 - r2):
        return False
    return True

# radius_sum test
def radius_sum(r1, r2):
    return r1 + r2

# hodnoty
x1, y1, r1 = 0, 0, 2
x2, y2, r2 = 3, 0, 2

fig, ax = plt.subplots()
circle1 = plt.Circle((x1, y1), r1, fill=False, color="blue")
circle2 = plt.Circle((x2, y2), r2, fill=False, color="red")

ax.add_patch(circle1)
ax.add_patch(circle2)
ax.set_xlim(-5, 8)
ax.set_ylim(-5, 5)

# zjistím si průnik
if has_intersection(x1, y1, r1, x2, y2, r2):
    print("Moje kružnice se protínají.")
else:
    print("Moje kružnice se neprotínají.")

plt.grid()
plt.show()
