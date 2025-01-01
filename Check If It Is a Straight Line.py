def check_straight_line_advanced(coordinates):
    """
    Check if all points in the coordinates list lie on a straight line in the XY plane.
    Advanced version with error handling and optimization.
    """
    # Ensure there are at least 2 points
    if len(coordinates) < 2:
        raise ValueError("At least two points are required to define a line.")
    
    # Validate the format of the input
    for point in coordinates:
        if len(point) != 2 or not all(isinstance(coord, (int, float)) for coord in point):
            raise ValueError("Each point must be a list or tuple of two numbers (x, y).")
    
    # Get the first two points to calculate the reference slope
    x1, y1 = coordinates[0]
    x2, y2 = coordinates[1]

    # Calculate the slope differences
    dx = x2 - x1
    dy = y2 - y1

    # Check collinearity for all points
    for i in range(2, len(coordinates)):
        x3, y3 = coordinates[i]
        # Using cross-product to check collinearity
        if (y3 - y1) * dx != (x3 - x1) * dy:
            return False  # Points are not collinear

    return True  # All points are collinear


# Example Usage with Advanced Scenarios
if __name__ == "__main__":
    try:
        # Example 1: Collinear Points
        coordinates1 = [[1, 2], [2, 3], [3, 4], [4, 5]]
        print(check_straight_line_advanced(coordinates1))  # Output: True

        # Example 2: Non-Collinear Points
        coordinates2 = [[1, 1], [2, 2], [3, 4], [4, 5]]
        print(check_straight_line_advanced(coordinates2))  # Output: False

        # Example 3: Invalid Input
        coordinates3 = [[1, 2], [2]]  # Invalid point
        print(check_straight_line_advanced(coordinates3))  # Raises ValueError

    except ValueError as e:
        print(f"Input Error: {e}")
