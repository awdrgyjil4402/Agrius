import csv

def Read(filepath):
    data = []
    with open(filepath, "r") as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            data.append(row)
    return data

def get_edge(row, col, map):
    rows = len(map)
    cols = len(map[0])
    neighbor_values = []

    # Define the relative positions of the eight neighbors
    neighbors = [
                (-1, 0),
        (0, -1),         (0, 1),
                 (1, 0)
    ]

    for dx, dy in neighbors:
        new_row = row + dx
        new_col = col + dy

        # Check if the neighbor position is within the grid bounds
        if 0 <= new_row < rows and 0 <= new_col < cols:
            neighbor_value = map[new_row][new_col]
            neighbor_values.append(neighbor_value)

    # Check if tile is exposed
    exposed = False
    for x in range(len(neighbor_values)):
        if x != '1':
            exposed = True

    if exposed:
        # Check tile neighbours
        pass
