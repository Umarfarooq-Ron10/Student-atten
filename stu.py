# Attendance Percentage Calculator

# Accept input from the user
classes_held = int(input("Enter the total number of classes held: "))
classes_attended = int(input("Enter the number of classes attended: "))

# Calculate attendance percentage
attendance_percentage = (classes_attended / classes_held) * 100

# Display the result
print(f"\nAttendance Percentage: {attendance_percentage:.2f}%")
