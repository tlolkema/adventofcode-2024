PHRASE = "MAS"


def build_grid(content):
    grid = []
    lines = content.strip().split("\n")
    for line in lines:
        grid.append(list(line))
    return grid


def find_matches(grid):
    matches = []
    grid_height = len(grid)
    grid_width = len(grid[0])

    for y in range(grid_height):
        for x in range(grid_width):
            if y > 0 and x > 0 and y < grid_height - 1 and x < grid_width - 1:
                # Start checking for A which is in the middle of the X
                if grid[y][x] == PHRASE[1]:
                    # Read the diagonals
                    diagonal1 = [grid[y - 1][x - 1], grid[y][x], grid[y + 1][x + 1]]
                    diagonal2 = [grid[y - 1][x + 1], grid[y][x], grid[y + 1][x - 1]]

                    # Convert diagonals to strings
                    d1 = "".join(diagonal1)
                    d2 = "".join(diagonal2)

                    # Check if either diagonal is MAS and the other is either MAS or SAM
                    if (d1 == "MAS" and (d2 == "MAS" or d2 == "SAM")) or (
                        d1 == "SAM" and (d2 == "MAS" or d2 == "SAM")
                    ):
                        matches.append({"x": x, "y": y})

    return matches


def main():
    with open("./day-4/input-full.txt") as file:
        content = file.read()
        grid = build_grid(content)
        matches = find_matches(grid)
        print(len(matches))


if __name__ == "__main__":
    main()
