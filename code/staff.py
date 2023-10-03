import sqlite3


class Staff:
    def __init__(self, staff_id, staff_name, staff_role):

        self.staff_id = staff_id
        self.staff_name = staff_name
        self.staff_role = staff_role

    def get_connection(database_name):
        try:
            conn = sqlite3.connect(database_name)
            return conn
        except sqlite3.Error as e:
            print(e)
            return None
        
    def create_table(database_name, table_name):
        conn = Staff.get_connection(database_name)
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

    def insert_staff(database_name, table_name, staff_name, staff_id, staff_role): 
        conn = Staff.get_connection(database_name)
        if conn:
            try: 
                cursor = conn.cursor()
                cursor.execute(f'''
                    INSERT INTO {table_name} (staff_name, staff_id)
                    VALUES (?, ?)
                ''', (staff_name, staff_id, staff_role))
                conn.commit()
                conn.close()
            except sqlite3.Error as e: 
                print(e)

    def display_staff(database_name, table_name): 
        conn = Staff.get_connection(database_name)
        if conn: 
            try: 
                cursor = conn.cursor()
                cursor.execute(f'''
                    SELECT staff_name, staff_id FROM {table_name}
                 ''' )
                staff = cursor.fetchall()
                for staff_member in staff: 
                    print(f"Staff Member Name: {staff_member[0]}, Staff ID: {staff_member[1]}, Staff Role: {staff_member[2]}")
                conn.close()
            except sqlite3.Error as e: 
                print(e)

