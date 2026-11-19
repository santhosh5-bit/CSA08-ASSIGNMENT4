from attendance import process_attendance

records = ["P", "A", "P", "P", "A", "P"]

present, absent = process_attendance(records)

print("Attendance Report")
print("Present:", present)
print("Absent:", absent)