def save_returns(books):
    log = open("returns.log", "w")

    for b in books:
        log.write(b)

    log.close()


def process(day_file):
    try:
        books = open(day_file, encoding="utf-8").read().split("\n")
        save_returns(books)

    except FileNotFoundError:
        print("missing")


process("day1.txt")
process("day2.txt")
process("day3.txt")

print("\nLog contents:")
with open("returns.log", "r", encoding="utf-8") as f:
    print(f.read())