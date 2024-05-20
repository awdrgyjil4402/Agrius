import csv
import random
from perlin_noise import PerlinNoise
from settings import *

def generate_map(filepath):
    noise = PerlinNoise(octaves=12, seed=SEED)
    grid_size = 150
    grid = []

    for i in range(grid_size):
        row = []
        for j in range(grid_size):
            if i == 0 or i == grid_size - 1 or j == 0 or j == grid_size - 1:
                row.append(str(-2))  # Wall
            else:
                noise_value = noise([i / grid_size, j / grid_size])
                if noise_value < -0.2:
                    row.append(str(-1))  # Water
                elif noise_value > 0.2:
                    row.append(str(1))  # Rock mountains
                else:
                    row.append(str(0))  # Ground
        grid.append(row)

    # Randomly select a "0" and turn it into a "2" to represent the player
    random_index_i = random.randint(1, grid_size - 2)
    random_index_j = random.randint(1, grid_size - 2)
    grid[random_index_i][random_index_j] = str(2)

    with open(filepath, "w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(grid)
    print('File generation complete.')

generate_map("../map/map.csv")
