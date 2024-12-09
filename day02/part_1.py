def main() -> int:
    total = 0
    with open("input.txt") as file:
        for line in file.readlines():
            line = line.split()
            if check_digits(line):
                total +=1
        return total

def check_digits(line: dict) -> bool:
    acs = (int(line[0]) - int(line[1])) < 0
    for digit in range(len(line)-1):
        diff = (int(line[digit]) - int(line[digit+1]))
        if  diff == 0 or (acs and (diff > -1 or diff < -3)) or (not acs and (diff < 1 or diff > 3)):          
            return False
    return True

print(f"Finished. Result {main()}")
