def read_file(filename: str) -> list:
    list = []
    with open(filename) as file:
        for line in file.readlines():
            list.append(line.split())
        return list


def winner(list: list):
    candidates = {}
    winner = ""
    max_votes = 0
    for el in list:
        if el[0] not in candidates.keys():
            candidates[el[0]] = 0
        if el[0] in candidates.keys():
            candidates[el[0]] += int(el[1])
    for key, value in candidates.items():
        if value >= max_votes:
            max_votes = value
            winner = key

    return f"Winner is {winner}"


if __name__ == "__main__":
    list_with_result = read_file("input (4).txt")
    print(winner(list_with_result))