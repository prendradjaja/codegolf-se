def mouse(grid):
    '''
    >>> mouse([ [ 4,  3,  2,  1], [ 5,  6,  7,  8], [12, 11, 10,  9], [13, 14, 15, 16] ])
    0
    >>> mouse([ [ 8,  1,  9, 14], [11,  6,  5, 16], [13, 15,  2,  7], [10,  3, 12,  4] ])
    0
    >>> mouse([ [ 1,  2,  3,  4], [ 5,  6,  7,  8], [ 9, 10, 11, 12], [13, 14, 15, 16] ])
    1
    >>> mouse([ [10, 15, 14, 11], [ 9,  3,  1,  7], [13,  5, 12,  6], [ 2,  8,  4, 16] ])
    3
    >>> mouse([ [ 3,  7, 10,  5], [ 6,  8, 12, 13], [15,  9, 11,  4], [14,  1, 16,  2] ])
    12
    >>> mouse([ [ 8,  9,  3,  6], [13, 11,  7, 15], [12, 10, 16,  2], [ 4, 14,  1,  5] ])
    34
    >>> mouse([ [ 8, 11, 12,  9], [14,  5, 10, 16], [ 7,  3,  1,  6], [13,  4,  2, 15] ])
    51
    >>> mouse([ [13, 14,  1,  2], [16, 15,  3,  4], [ 5,  6,  7,  8], [ 9, 10, 11, 12] ])
    78
    >>> mouse([ [ 9, 10, 11, 12], [ 1,  2,  4, 13], [ 7,  8,  5, 14], [ 3, 16,  6, 15] ])
    102
    >>> mouse([ [ 9, 10, 11, 12], [ 1,  2,  7, 13], [ 6, 16,  4, 14], [ 3,  8,  5, 15] ])
    103
    '''
    pos = [
        (r, c)
        for (r, row) in enumerate(grid)
        for (c, value) in enumerate(row)
        if value == 16
    ][0]
    while True:
        setindex(grid, pos, 0)
        all_neighbors = [
            addvec(pos, offset)
            for offset in [
                (-1, -1), (-1,  0), (-1,  1),
                ( 0, -1),           ( 0,  1),
                ( 1, -1), ( 1,  0), ( 1,  1),
            ]
        ]
        neighbors = [
            nei for nei in all_neighbors
            if in_bounds(grid, nei) and getindex(grid, nei)
        ]
        if not neighbors:
            break
        pos = max(neighbors, key=lambda nei: getindex(grid, nei))
    return sum(value for row in grid for value in row)


def addvec(v, w):
    return (v[0] + w[0], v[1] + w[1])


def getindex(grid, pos):
    r, c = pos
    return grid[r][c]


def setindex(grid, pos, value):
    r, c = pos
    grid[r][c] = value


def in_bounds(grid, pos):
    r, c = pos
    return (
        0 <= r < len(grid) and
        0 <= c < len(grid[0])
    )
