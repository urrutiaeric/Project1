import sqlite3
class Students:

    def __init__(self, name, idnum, courses, gpa, database, table):
        self.name = name
        self.idnum = idnum
        self.courses = courses
        self.gpa = gpa
        self.database = "student.db"
        self.table = "Student"
        
    def get_connection(self.database):
        try:
            conn = sqlite3.connect(self.database)
            return conn
        except sqlite3.Error as e:
            print(e)
            return None

    
    def create_table(self.database, self.table):
        conn = Student.get_connection(self.database)
        if conn:
            try:
                cursor = conn.cursor()
                cursor.execute(f'''
                    CREATE TABLE IF NOT EXISTS {self.table} (
                        id INTEGER PRIMARY KEY,
                        student_name TEXT,
                        student_id INTEGER,
                        student_courses TEXT,
                        student_gpa FLOAT
                    )
                ''')
                conn.commit()
                conn.close()
            except sqlite3.Error as e:
                print(e)

    def add_student(name):
        flagvalidation = True
        student_name = t1.get("1.0", END)
        student_idnum = t2.get("1.0", END)
        conn = Student.get_connection(self.database)
        create_student = f''' INSERT INTO Student(student_name, student_id) VALUES({student_name},{student_idnum})'''
        curr = conn.cursor()
        curr.execute(create_student)
        conn.commit
        return curr.lastrowid

    def add_courses()
    
    
    