def process_mess_bill(filename):
    total = 0
    report = []
    rejected_lines = []

    try:
        with open(filename, "r", encoding="utf-8") as f:
            for line_number, line in enumerate(f, start=1):
                if not line.strip():
                    continue

                try:
                    parts = line.strip().split(",")

                    if len(parts) != 3:
                        raise ValueError("Expected 3 fields")

                    register_number, name, amount = parts
                    amount = float(amount)

                    total += amount
                    report.append(f"{name} {amount}")

                except (ValueError, IndexError) as e:
                    rejected_lines.append(
                        f"Line {line_number}: {line.strip()} - {e}"
                    )

    except FileNotFoundError:
        print("File not found.")
        return

    print("Mess Bill Report")
    for item in report:
        print(item)

    print("Total:", total)

    print("\nRejected Lines:")
    for item in rejected_lines:
        print(item)


process_mess_bill("mess_oct.txt")