from src.geometry import has_intersection, radius_sum


def test_has_intersection_normal_1():
    assert has_intersection(0, 0, 5, 6, 0, 5) is True


def test_has_intersection_normal_2():
    assert has_intersection(1, 1, 3, 4, 1, 2) is True


def test_has_intersection_boundary_1():
    assert has_intersection(0, 0, 5, 10, 0, 5) is True


def test_has_intersection_boundary_2():
    assert has_intersection(0, 0, 5, 0, 0, 5) is True


def test_has_intersection_negative():
    assert has_intersection(0, 0, 2, 10, 0, 2) is False


def test_radius_sum():
    assert radius_sum(4, 7) == 11