
import os
import sqlite3

student_id = 123
courses = "math"
grade = 98

conn = sqlite3.connect("example.db")
cursor = conn.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS student (
                    student_id INTEGER PRIMARY KEY,
                    courses TEXT,
                    grade INTEGER
                )''')
conn.commit()


# push data 
cursor.execute("INSERT INTO student (student_id, courses, grade) VALUES (?, ?, ?)",
                       (student_id, courses, grade))
conn.commit()

# to display 
cursor.execute("SELECT * FROM student")
data = cursor.fetchall()

os.system("cls")

if not data:
    print("unable to fetch data")
else:
    for row in data:
            print("student is   | Courses     | Grade  ")
            print(f"{row[0]:13} | {row[1]:10} | {row[2]:17} ")


conn.close()