import re


def main():
    with open("./day-3/input-full.txt") as file:
        content = file.read()

    clean_content = content.replace("\n", "")
    clean_content = re.sub(r"don't\(\).*?do\(\)", "", content)
    clean_content = clean_content[: clean_content.find("don't()")]

    matches = re.findall(r"mul\(\d+,\d+\)", clean_content)
    clean_matches = [match.replace("mul(", "").replace(")", "") for match in matches]

    multiplications = [
        int(match.split(",")[0]) * int(match.split(",")[1]) for match in clean_matches
    ]
    print(sum(multiplications))


if __name__ == "__main__":
    main()
