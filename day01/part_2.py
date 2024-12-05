
def main():
    teamA = []
    teamB = []
    total = 0
    with open("input.txt") as file:
        for line in file.readlines():
            line = line.split()
            teamA.append(line[0])
            teamB.append(line[1])
    assert len(teamA) == len(teamB)
    teamA.sort()
    teamB.sort()
    for number in teamA:
        occurances = teamB.count(number)
        total += int(number) * occurances
    return total

print("Start")
total = main()
print(f"Finished. Result {total}")
