PHRASE = "XMAS"


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
            # Horizontal forward
            if x + len(PHRASE) <= grid_width:
                forward_phrase = "".join(grid[y][x : x + len(PHRASE)])
                if forward_phrase == PHRASE:
                    matches.append({"x": x, "y": y})

            # Horizontal backward
            if x - len(PHRASE) + 1 >= 0:
                backward_phrase = "".join(grid[y][x : x - len(PHRASE) : -1])
                if backward_phrase == PHRASE:
                    matches.append({"x": x, "y": y})

            # Vertical forward
            if y + len(PHRASE) <= grid_height:
                forward_phrase = "".join(grid[y + i][x] for i in range(len(PHRASE)))
                if forward_phrase == PHRASE:
                    matches.append({"x": x, "y": y})

            # Vertical backward
            if y - len(PHRASE) + 1 >= 0:
                backward_phrase = "".join(grid[y - i][x] for i in range(len(PHRASE)))
                if backward_phrase == PHRASE:
                    matches.append({"x": x, "y": y})

            # Diagonal down-right
            if x + len(PHRASE) <= grid_width and y + len(PHRASE) <= grid_height:
                diagonal_phrase = "".join(
                    grid[y + i][x + i] for i in range(len(PHRASE))
                )
                if diagonal_phrase == PHRASE:
                    matches.append({"x": x, "y": y})

            # Diagonal down-left
            if x - len(PHRASE) + 1 >= 0 and y + len(PHRASE) <= grid_height:
                diagonal_phrase = "".join(
                    grid[y + i][x - i] for i in range(len(PHRASE))
                )
                if diagonal_phrase == PHRASE:
                    matches.append({"x": x, "y": y})

            # Diagonal up-right
            if x + len(PHRASE) <= grid_width and y - len(PHRASE) + 1 >= 0:
                diagonal_phrase = "".join(
                    grid[y - i][x + i] for i in range(len(PHRASE))
                )
                if diagonal_phrase == PHRASE:
                    matches.append({"x": x, "y": y})

            # Diagonal up-left
            if x - len(PHRASE) + 1 >= 0 and y - len(PHRASE) + 1 >= 0:
                diagonal_phrase = "".join(
                    grid[y - i][x - i] for i in range(len(PHRASE))
                )
                if diagonal_phrase == PHRASE:
                    matches.append({"x": x, "y": y})

    return matches


def main():
    with open("./day-4/input-small.txt") as file:
        content = file.read()
        grid = build_grid(content)
        matches = find_matches(grid)
        print(len(matches))


if __name__ == "__main__":
    main()
