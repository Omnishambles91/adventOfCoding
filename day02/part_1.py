def main() -> int:
    total = 0
    with open("input.txt") as file:
        for line in file.readlines():
            line = line.split()
            if check_digits(line):
                total +=1
        return total

def check_digits(line: dict) -> bool:
    direction = int(line[0]) - int (line[1])
    if direction == 0:
        return False
    ascending = direction < 0
    for digit in range(len(line) -1):
        difference = (int(line[digit]) - int(line[digit+1]))
        if difference == 0 or (ascending and difference > -1 and difference < -3) or (not ascending and difference > 1 and difference < 3):
            return False
    return True

print(f"Finished. Result {main()}")
