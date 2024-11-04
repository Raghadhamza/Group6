def analyze_curtain_wall_windows(curtain_walls):
    windows = []
    for wall in curtain_walls:
        windows.extend(wall.IsDefinedBy)  # Adjust based on actual attributes
    result = f"Windows in Curtain Walls: {len(windows)}"
    return windows, result
