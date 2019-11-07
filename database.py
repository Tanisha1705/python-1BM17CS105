import sqlite3

try:
    connection = sqlite3.connect('database')
    cur = connection.cursor()
except:
    print("Database already exists")

class student_database:
    def __init__(self):
        pass

    def create_table(self):
        cur.execute("""CREATE TABLE students (id INTEGER PRIMARY KEY,
                        name TEXT,
                        marks TEXT,
                        percentage TEXT)""")

    def add_info(self, idd, name, marks, percentage):
        cur.execute("""INSERT INTO students VALUES (%d, '%s', '%s', '%s') """ %(idd, name, marks, percentage))

    def display_all(self):
        cur.execute("""SELECT * FROM students""")
        stuff = cur.fetchall()
        return stuff

    def del_student(self, idd):
        cur.execute("""DELETE FROM students WHERE id = %d""" %(idd))

    def update_student(self,idd, marks, percentage):
        cur.execute("""UPDATE students SET marks = %s, percentage = %s WHERE id = %d""" %(marks, percentage, idd))

    def get_student(self, idd):
        cur.execute("""SELECT * FROM students WHERE id = %d""" %(idd))
        tup = cur.fetchall()
        return tup


db = student_database()
try:
    db.create_table()
except:
    pass
db.add_info(1, "sudarshan", 100, 99)
db.add_info(2, "Sud", 150, 100)
db.add_info(3, "Siddharth", 10, 3)
db.add_info(4, "Tanisha", 3, 10)
print(db.display_all())
db.update_student(3, 100, 30)
print(db.display_all())
db.del_student(4)
print(db.display_all())
print(db.get_student(1))
