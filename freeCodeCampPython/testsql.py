import sqlite3

conn = sqlite3.connect('pydb.db')
cur = conn.cursor()

selectAll = ''' SELECT User.name, Member.role, Course.title
            FROM User JOIN Member JOIN Course
            ON Member.user_id = User.id AND Member.course_id = Course.id
            ORDER BY Course.title, Member.role DESC, User.name '''

for row in cur.execute(selectAll):
    print(row)

cur.close()