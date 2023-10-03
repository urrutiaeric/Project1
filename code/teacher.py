import sqlite3

class Teacher:
    def __init__(self, teacher_id, teacher_name, courses_taught):
        self.teacher_id = teacher_id
        self.teacher_name = teacher_name
        self.courses_taught = courses_taught

    def get_connection(database_name):
        try:
            conn = sqlite3.connect(database_name)
            return conn
        except sqlite3.Error as e:
            print(e)
            return None
        
    def create_table(database_name, table_name):
        conn = Teacher.get_connection(database_name)
        if conn: 
            try:
                cursor = conn.cursor()
                cursor.execute(f'''
                               CREATE TABLE IF NONE EXISTS {table_name} (id INTEGER PRIMARY KEY, teacher_id TEXT, teacher_name TEXT, courses_taught TEXT)''')
                conn.commit()
                conn.close()
            except sqlite3.Error as e:
                print(e)

    def insert_teacher(database_name, table_name, teacher_id, teacher_name, courses_taught):
        conn = Teacher.gett_connection(database_name)
        if conn:
            try:
                cursor = conn.cursor()
                cursor.execute(f'''
                               INSERT INTO {table_name} (teacher_id, teacher_name, courses_taught)
                               VALUES (?, ?)
                               ''', (teacher_id, teacher_name, courses_taught))
                conn.commit()
                conn.close()
            except sqlite3.Error as e:
                print(e)

    def display_teachers(database_name, table_name):
        conn = Teacher.get_connection(database_name)
        if conn:
            try:
                cursor = conn.cursor()
                cursor.execute(f'''
                               SELECT teacher_id, teacher_name, courses_taught FROM {table_name}
                               ''')
                teachers = cursor.fetchall()
                for teacher in teachers:
                    print(f"Teacher ID: {teacher[0]}, Teacher Name: {teacher[1]}, Courses Taught: {teacher[2]}")
                    conn.close()
            except sqlite3.Error as e:
                print(e)

    def get_teacher_id(teacher_id):
        return teacher_id
    
    def get_teacher_name(teacher_name):
        return teacher_name
    
    def get_courses_taught(courses_taught):
        return courses_taught
    
