def main():
    with open("names.txt", encoding="utf-8") as file:
        file.readline()
        for line in file:
            line = line.strip().split()
            conjunto = {line[i] for i in range(0, len(line)-1)}
            print(f"{line[len(line)-1]} : {conjunto}")

main()