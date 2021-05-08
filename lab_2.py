from matplotlib import pyplot as plt
from math import atan, degrees


def get_slope(p1, p2):
    if p2.x - p1.x == 0:
        return float('inf')
    slope = (p2.y - p1.y) / (p2.x - p1.x)
    return slope


def get_angle(b_point, p):
    angle = degrees(atan(get_slope(b_point, p)))
    if angle < 0:
        angle += 180
    return angle


def plot_graph(points, title='Graph Plot'):
    plt.plot([p.x for p in points], [p.y for p in points])
    for p in points:
        plt.text(p.x, p.y, '({}, {})'.format(p.x, p.y))
    plt.xlabel("x axis")
    plt.ylabel("y axis")
    plt.title(title)
    plt.show()


class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.previous = None
        self.next = None

    def __str__(self):
        return f"({self.x}, {self.y})"


class Polygon:
    vertex = None
    start = None

    @property
    def points(self):
        if self.vertex is not None:
            points = [self.vertex]
            p = self.vertex.next
            while p is not self.vertex:
                points.append(p)
                p = p.next
            return points
        else:
            return []

    def angular_sorting(self, points):
        b_point = points[0]
        print("b_point", b_point.x, b_point.y)
        result = []
        for p in points[1:]:
            print(p.x, p.y)
            angle = get_angle(b_point, p)
            result.append((p, angle))
        result = sorted(result, key=lambda x: x[1])
        points = [(b_point, 0)]
        points.extend(result)
        return points

    def add_vertices(self, points):
        if len(points) < 3:
            print("Polygon must have at least 3 vertices")
        points = sorted(points, key=lambda p: p.y)
        points = self.angular_sorting(points)
        points = [item[0] for item in points]
        print([(p.x, p.y) for p in points])
        end_vertex = None
        for point in points:
            if self.vertex is None:
                self.vertex = point
            else:
                point.previous = self.vertex
                end_vertex.next = point
            end_vertex = point
        end_vertex.next = self.vertex

    def is_vertex(self, point):
        for p in self.points:
            if p.x == point.x and p.y == point.y:
                return True
        return False

    def plot(self):
        points = self.points
        points.append(self.points[0])
        plot_graph(points, 'Polygon Plot')


def user_input():
    input_str = []
    print("ENTER VERTICES \npress q after you complete your vertices\n")
    while 1:
        item = input()
        if item == 'q':
            break
        items = item.split(',') if item.find(',') >= 0 else item.split()
        if len(items) == 2:
            try:
                a = int(items[0])
                b = int(items[1])
                input_str.append((a, b))
            except Exception as exc:
                print("Enter point coordinate as number")
        else:
            print("Invalid input point")
    return input_str


def turn_test(p0, p1, p2):
    area = (p1.x - p0.x)*(p2.y-p0.y) - (p2.x-p0.x)*(p1.y-p0.y)
    if area < 0:
        return "right"
    elif area > 0:
        return "left"
    else:
        return "collinear"


def is_poly_convex(polygon):
    points = polygon.points
    point_len = len(points)
    check_turn = "left"
    for i, p in enumerate(points):
        if i == point_len-1:
            break
        third_idx = 0 if i == point_len -2 else i+2
        turn_result = turn_test(p, points[i+1], points[third_idx])
        if not turn_result == 'collinear':
            if not check_turn == turn_result:
                return False
    return True


def main():
    input_str = user_input()
    # # input_str = [(1, 1), (2, 2), (3, 3), (5, 8), (1, 3)]
    # # input_str = [(1, 1), (3, 3), (5, 6), (7, 8), (2, 4), (1, 5)]
    # input_str = [(7, 5), (1,5), (5,12), (2, 1), (5, 1), (2, 12)]
    # input_str = [(3, 5), (1,5), (5,12), (2, 1), (5, 1), (2, 12)]
    points = []
    for point in input_str:
        points.append(Point(x=point[0], y=point[1]))

    poly = Polygon()
    poly.add_vertices(points)

    is_convex = is_poly_convex(poly)

    convex_str = "a convex" if is_convex else "not a convex"
    print(f"Given Polygon is {convex_str} polygon")
    poly.plot()
