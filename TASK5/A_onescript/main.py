def process_attendance(records):
    present = 0
    absent = 0

    for status in records:
        if status == "P":
            present += 1
        elif status == "A":
            absent += 1

    print("Attendance Report")
    print("Present:", present)
    print("Absent:", absent)


records = ["P", "A", "P", "P", "A", "P"]

process_attendance(records)