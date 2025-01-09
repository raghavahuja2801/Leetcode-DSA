import math

def closest_pair_of_points(points):
    def distance(p1, p2):
        return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

    def closest_pair_rec(points_sorted_by_x, points_sorted_by_y):
        if len(points_sorted_by_x) <= 3:
            return brute_force_closest_pair(points_sorted_by_x)

        mid = len(points_sorted_by_x) // 2
        left_x = points_sorted_by_x[:mid]
        right_x = points_sorted_by_x[mid:]

        median_x = points_sorted_by_x[mid][0]
        left_y, right_y = [], []
        for p in points_sorted_by_y:
            if p[0] <= median_x:
                left_y.append(p)
            else:
                right_y.append(p)

        left_pair = closest_pair_rec(left_x, left_y)
        right_pair = closest_pair_rec(right_x, right_y)

        min_pair = min(left_pair, right_pair, key=lambda pair: distance(pair[0], pair[1]))

        strip = [p for p in points_sorted_by_y if abs(p[0] - median_x) < distance(min_pair[0], min_pair[1])]
        min_pair = min(min_pair, closest_pair_in_strip(strip, min_pair), key=lambda pair: distance(pair[0], pair[1]))

        return min_pair

    def closest_pair_in_strip(strip, best_pair):
        min_dist = distance(best_pair[0], best_pair[1])
        for i in range(len(strip)):
            for j in range(i + 1, len(strip)):
                if strip[j][1] - strip[i][1] >= min_dist:
                    break
                min_dist = min(min_dist, distance(strip[i], strip[j]))
        return best_pair

    def brute_force_closest_pair(points):
        min_dist = float('inf')
        closest_pair = None
        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                d = distance(points[i], points[j])
                if d < min_dist:
                    min_dist = d
                    closest_pair = (points[i], points[j])
        return closest_pair

    points_sorted_by_x = sorted(points, key=lambda p: p[0])
    points_sorted_by_y = sorted(points, key=lambda p: p[1])

    return closest_pair_rec(points_sorted_by_x, points_sorted_by_y)

# Example usage
points = [(0, 0), (3, 4), (5, 6), (7, 8), (1, 2)]
print(closest_pair_of_points(points))  # Output: The closest pair of points
