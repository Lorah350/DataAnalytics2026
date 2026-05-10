# show_major.py
# This script stores a student's name and major code,
# then uses if/elif logic to look up the major name and department location.
# If the major code isn't recognized, we show <unknown>.

# -----------------------------
# 1. Student info (change these to test)
# -----------------------------
student_name = "Lorah"
student_major = "ENG"   # try ENG, BUS, MKT, CSC, or something fake like XYZ

# -----------------------------
# 2. Lookup logic for major + location
# -----------------------------
# Start by assuming we don't know the major
major_name = "<unknown>"
major_location = ""

# Now check each valid major code
if student_major == "ENG":
    major_name = "English"
    major_location = "Building A, Room 101"

elif student_major == "BUS":
    major_name = "Business Administration"
    major_location = "Building B, Room 225"

elif student_major == "MKT":
    major_name = "Marketing"
    major_location = "Building C, Room 310"

elif student_major == "CSC":
    major_name = "Computer Science"
    major_location = "Tech Center, Room 12"

# If none of the above match, major_name stays <unknown>
# and major_location stays empty — exactly what the assignment requires.

# -----------------------------
# 3. Display results
# -----------------------------
print("Student Name:", student_name)
print("Major Code:", student_major)
print("Major Name:", major_name)
print("Department Location:", major_location)
