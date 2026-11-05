def print_3d_cube(size=2.0):
    half = size / 2.0
    vertices = [
        (-half, -half, -half),
        (half, -half, -half),
        (half, half, -half),
        (-half, half, -half),
        (-half, -half, half),
        (half, -half, half),
        (half, half, half),
        (-half, half, half)
    ]
    edges = [
        (0, 1), (1, 2), (2, 3), (3, 0),
        (4, 5), (5, 6), (6, 7), (7, 4),
        (0, 4), (1, 5), (2, 6), (3, 7)
    ]
    print(f"\n--- 3D Cube Vertices (Size: {size}) ---")
    print("ID\tX\tY\tZ")
    for i, (x, y, z) in enumerate(vertices):
        print(f"{i}\t{x:+.1f}\t{y:+.1f}\t{z:+.1f}")
    print("\n--- 3D Cube Edges ---")
    for edge in edges:
        v1 = vertices[edge[0]]
        v2 = vertices[edge[1]]
    print(f"Edge from vertex {edge[0]} {v1} "
              f"to vertex {edge[1]} {v2}")


# Call the function
print_3d_cube(2.0)