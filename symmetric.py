points_tuples = [(1, 2), (3, 2), (0, 1), (4, 1), (2, 3)]

def is_sym(points_tuples):
    assym_max = max([p[0] for p in points_tuples])
    assym_min = min([p[0] for p in points_tuples])
    mid = (assym_max + assym_min) / 2
    for point in points_tuples:
        px = 2 * mid - point[0]
        py = point[1]
        if (point[0] != px) and (px, py) not in points_tuples:
            return False
    return True

print(is_sym(points_tuples))
