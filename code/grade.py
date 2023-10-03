import sqlite3

class Grade:
    def __init__(self, student_id, course_id, grade):
        self.student_id = student_id
        self.course_id = course_id
        self.grade = grade
        
    def get_connection(database_name):
        try:
            conn = sqlite3.connect(database_name)
            return conn
        except sqlite3.Error as e:
            print(e)
            return None
        
    def create_table(database_name, table_name):
        conn = Grade.get_connection(database_name)
        if conn:
            try:
                cursor = conn.cursor()
                cursor.execute(f'''
                               CREATE TABLE IF NONE EXISTS {table_name}
                               (id INTEGER PRIMARY KEY,
                               student_id TEXT, 
                               course_id TEXT,
                               grade TEXT)''')
                conn.commit()
                conn.close()
            except sqlite3 as e:
                print(e)
    
    def insert_grade(database_name, table_name, student_id, course_id, grade):
        conn = Grade.get_connection(database_name)
        if conn:
            try:
                cursor = conn.cursor()
                cursor.execute(f'''
                               INSERT INTO {table_name} (student_id, course_id, grade)
                               VALUES (?, ?, ?)
                               ''', (student_id, course_id, grade))
                conn.commit()
                conn.close()
            except sqlite3.Error as e:
                print(e)
    
    def display_grades(database_name, table_name):
        conn = Grade.get_connection(database_name)
        if conn:
            try: 
                cursor = conn.cursor()
                cursor.execute(f'''
                               SELECT student_id, course_id, grade FROM {table_name}
                               ''')
                grades = cursor.fetchall()
                for grade in grades:
                    print (f"Course ID: {grade[0]}, Student ID: {grade[1]}, Grade: {grade[2]}")
                conn.close()
            except sqlite3.Error as e:
                print(e)

    def get_student_id(student_id):
        return student_id
    
    def get_course_id(course_id):
        return course_id
    
    def get_grade(grade):
        return grade