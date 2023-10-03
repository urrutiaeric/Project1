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
        conn = Course.get_connection(self.database)
        if conn:
            try:
                cursor = conn.cursor()
                cursor.execute(f'''
                    CREATE TABLE IF NOT EXISTS {self.table} (
                        id INTEGER PRIMARY KEY,
                        student_name TEXT,
                        student id INTEGER,
                        student_courses TEXT,
                        student_gpa FLOAT
                    )
                ''')
                conn.commit()
                conn.close()
            except sqlite3.Error as e:
                print(e)

    def add_student(name):
        

        return name
    
    
    