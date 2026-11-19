def process_attendance(records):
    present = records.count("P")
    absent = records.count("A")

    return present, absent