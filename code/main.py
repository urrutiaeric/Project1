from course import *

# Example usage:
database_name = "course.db"
table_name = "course"
Course.create_table(database_name, table_name)
Course.insert_course(database_name, table_name, "Computer Science", "CS101")
Course.insert_course(database_name, table_name, "Mathematics", "MATH101")

# Display courses from the database
Course.display_courses(database_name, table_name)
