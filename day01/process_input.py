
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
    for i in range(len(teamA)): 
        total += abs(int(teamA[i]) - int(teamB[i]))
    return total

print("Start")
total = main()
print(f"Finished. Result {total}")
