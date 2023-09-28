
import os
import sqlite3

student_id = 123
courses = "math"
grade = 98

conn = sqlite3.connect("example.db")
cursor = conn.cursor()

import customtkinter as ctk
 
# Sets the appearance mode of the application
# "System" sets the appearance same as that of the system
ctk.set_appearance_mode("System")       
 
# Sets the color of the widgets
# Supported themes: green, dark-blue, blue
ctk.set_default_color_theme("green")   
 
# Create App class
class App(ctk.CTk):
# Layout of the GUI will be written in the init itself
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
# Sets the title of our window to "App"
        self.title("App")   
# Dimensions of the window will be 200x200
        self.geometry("200x200")   
 
 
if __name__ == "__main__":
    app = App()
    # Runs the app
    app.mainloop()   
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