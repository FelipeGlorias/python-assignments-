def cacti_number(func):
    def wrapper():
        grid = func()
        if not isinstance(grid, list):
            raise TypeError("Grid must be a list")
        if len(grid) == 0:
            return 0
        rows = len(grid)
        cols = len(grid[0])
        for row in grid:
            if not isinstance(row, list):
                raise TypeError("Each row must be a list")
            if len(row) != cols:
                raise TypeError("All rows must have the same length")
            for cell in row:
                if cell not in (0, 1):
                    raise TypeError("All cells must be 0 or 1")
        working_grid = [row[:] for row in grid]
        count = 0
        for r in range(rows):
            for c in range(cols):
                if working_grid[r][c] == 0 and _can_place(working_grid, r, c, rows, cols):
                    working_grid[r][c] = 1
                    count += 1
        return count
    return wrapper

def _can_place(grid, r, c, rows, cols):
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    for dr, dc in directions:
        nr, nc = r + dr, c + dc
        if 0 <= nr < rows and 0 <= nc < cols:
            if grid[nr][nc] == 1:
                return False
    return True
