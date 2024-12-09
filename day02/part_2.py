def main() -> int:
    total = 0
    with open("input.txt") as file:
        for line in file.readlines():
            line = line.split()
            tolerance = check_digits(line)
            if tolerance == 0:
                total +=1
            else:
                line.pop(tolerance)
                if check_digits(line) == 0:
                    total += 1
        return total

def check_digits(line: dict) -> bool:
    direction = int(line[0]) - int (line[1])
    if direction == 0:
        return 1
    ascending = direction < 0
    for digit in range(len(line) -1):
        difference = (int(line[digit]) - int(line[digit+1]))
        if difference == 0 or (ascending and difference > -1 and difference < -3) or (not ascending and difference < 1 and difference > 3):
            print(line)
            print(f"direction: {ascending}")
            print(f"difference: {difference}")
            return (int(digit))
    return 0

print(f"Finished. Result {main()}")
