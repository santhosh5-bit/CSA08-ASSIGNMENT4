import csv
import os

INPUT_FOLDER = "input"
OUTPUT_FOLDER = "department_reports"

os.makedirs(OUTPUT_FOLDER, exist_ok=True)

valid_records = []
seen_registers = set()
errors = []

files = ["cse.csv", "ece.csv", "it.csv", "damaged.csv"]

for filename in files:
    filepath = os.path.join(INPUT_FOLDER, filename)

    try:
        with open(filepath, "r", encoding="utf-8") as f:
            reader = csv.reader(f)
            next(reader, None)

            for line_number, row in enumerate(reader, start=2):
                try:
                    if len(row) != 4:
                        raise ValueError("Incorrect number of fields")

                    reg, name, email, department = row

                    if not email or "@" not in email:
                        raise ValueError("Invalid email")

                    if reg in seen_registers:
                        raise ValueError("Duplicate register number")

                    seen_registers.add(reg)
                    valid_records.append(row)

                except ValueError as e:
                    errors.append(f"{filename}, Line {line_number}: {e}")

    except FileNotFoundError:
        errors.append(f"Missing file: {filename}")


# Create master file
with open("master.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["RegisterNumber", "Name", "Email", "Department"])
    writer.writerows(valid_records)


# Create department-wise reports
departments = {}

for record in valid_records:
    department = record[3]
    departments.setdefault(department, []).append(record)

for department, records in departments.items():
    path = os.path.join(OUTPUT_FOLDER, department + ".csv")

    with open(path, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["RegisterNumber", "Name", "Email", "Department"])
        writer.writerows(records)


# Create summary
with open("summary.txt", "w", encoding="utf-8") as f:
    f.write("Registration Summary\n")
    f.write(f"Total Valid Records: {len(valid_records)}\n")

    for department, records in departments.items():
        f.write(f"{department}: {len(records)}\n")


# Create error log
with open("error_log.txt", "w", encoding="utf-8") as f:
    for error in errors:
        f.write(error + "\n")


print("Processing completed.")
print("Valid records:", len(valid_records))
print("Errors:", len(errors))
print("Master file created.")
print("Department reports created.")
print("Summary created.")
print("Error log created.")