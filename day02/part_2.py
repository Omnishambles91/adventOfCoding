def main() -> int:
    with open("input.txt") as file:
        for line in file.readlines().split():
            code = check_digits(line)
            if code != 0:
                line.pop(code - 1)
                code = check_digits(line)
        if code == 0: total += 1
        return total

def check_digits(line: dict) -> bool:
    # Determine if numbers are increasing or decreasing, 0 fails by default
    direction = int(line[0]) - int (line[1])
    if direction == 0: 
        return 1
    asc = true if direction < 0 else asc = False
    # return false if difference is 0 or positive/negative when opposite is expected
    for digit in range(len(line) -1):
        diff = (int(line[digit]) - int(line[digit+1]))
        if direction == 0 or (asc and -3 > diff < 0) or (not asc and 3 < diff > 0):
            return int(line[digit])
    return 0

print(f"Result {main()}")
