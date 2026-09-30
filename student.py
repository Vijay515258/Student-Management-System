import sqlite3


# -------------------- ADD STUDENT --------------------
def add_student():
    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()

    name = input("Enter Student Name: ")
    age = int(input("Enter Student Age: "))
    course = input("Enter Course: ")
    marks = int(input("Enter Marks: "))

    cursor.execute(
        """
        INSERT INTO students(name, age, course, marks)
        VALUES (?, ?, ?, ?)
        """,
        (name, age, course, marks)
    )

    conn.commit()
    conn.close()

    print("\nStudent added successfully!")


# -------------------- VIEW STUDENTS --------------------
def view_students():
    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM students")
    students = cursor.fetchall()

    print("\n==============================")
    print("      STUDENT RECORDS")
    print("==============================")

    if len(students) == 0:
        print("No student records found.")
    else:
        print(f"{'ID':<5}{'NAME':<20}{'AGE':<8}{'COURSE':<15}{'MARKS'}")
        print("-" * 60)

        for student in students:
            print(f"{student[0]:<5}{student[1]:<20}{student[2]:<8}{student[3]:<15}{student[4]}")

    conn.close()


# -------------------- SEARCH STUDENT --------------------
def search_student():
    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()

    student_id = int(input("Enter Student ID to Search: "))

    cursor.execute("SELECT * FROM students WHERE id = ?", (student_id,))
    student = cursor.fetchone()

    if student:
        print("\nStudent Found")
        print("------------------------")
        print("ID     :", student[0])
        print("Name   :", student[1])
        print("Age    :", student[2])
        print("Course :", student[3])
        print("Marks  :", student[4])
    else:
        print("\nStudent not found.")

    conn.close()


# -------------------- UPDATE STUDENT --------------------
def update_student():
    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()

    student_id = int(input("Enter Student ID to Update: "))

    cursor.execute("SELECT * FROM students WHERE id = ?", (student_id,))
    student = cursor.fetchone()

    if student:
        name = input("Enter New Name: ")
        age = int(input("Enter New Age: "))
        course = input("Enter New Course: ")
        marks = int(input("Enter New Marks: "))

        cursor.execute(
            """
            UPDATE students
            SET name=?, age=?, course=?, marks=?
            WHERE id=?
            """,
            (name, age, course, marks, student_id)
        )

        conn.commit()
        print("\nStudent updated successfully!")

    else:
        print("\nStudent not found.")

    conn.close()


# -------------------- DELETE STUDENT --------------------
def delete_student():
    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()

    student_id = int(input("Enter Student ID to Delete: "))

    cursor.execute("SELECT * FROM students WHERE id=?", (student_id,))
    student = cursor.fetchone()

    if student:
        cursor.execute("DELETE FROM students WHERE id=?", (student_id,))
        conn.commit()
        print("\nStudent deleted successfully!")
    else:
        print("\nStudent not found.")

    conn.close()