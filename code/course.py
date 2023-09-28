import sqlite3

class Course:
    def __init__(self, course_name, course_id):
        self.course_name = course_name
        self.course_id = course_id

    
    def get_connection(database_name):
        try:
            conn = sqlite3.connect(database_name)
            return conn
        except sqlite3.Error as e:
            print(e)
            return None

    
    def create_table(database_name, table_name):
        conn = Course.get_connection(database_name)
        if conn:
            try:
                cursor = conn.cursor()
                cursor.execute(f'''
                    CREATE TABLE IF NOT EXISTS {table_name} (
                        id INTEGER PRIMARY KEY,
                        course_name TEXT,
                        course_id TEXT
                    )
                ''')
                conn.commit()
                conn.close()
            except sqlite3.Error as e:
                print(e)
 
    
    def insert_course(database_name, table_name, course_name, course_id):
        conn = Course.get_connection(database_name)
        if conn:
            try:
                cursor = conn.cursor()
                cursor.execute(f'''
                    INSERT INTO {table_name} (course_name, course_id)
                    VALUES (?, ?)
                ''', (course_name, course_id))
                conn.commit()
                conn.close()
            except sqlite3.Error as e:
                print(e)

    
    def display_courses(database_name, table_name):
        conn = Course.get_connection(database_name)
        if conn:
            try:
                cursor = conn.cursor()
                cursor.execute(f'''
                    SELECT course_name, course_id FROM {table_name}
                ''')
                courses = cursor.fetchall()
                for course in courses:
                    print(f"Course Name: {course[0]}, Course ID: {course[1]}")
                conn.close()
            except sqlite3.Error as e:
                print(e)

