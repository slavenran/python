import sqlite3
import json

conn = sqlite3.connect('rosterdb.sqlite')
cur = conn.cursor()

cur.executescript('''DROP TABLE IF EXISTS User;
DROP TABLE IF EXISTS Member;
DROP TABLE IF EXISTS Course;

CREATE TABLE User (
    id     INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name   TEXT UNIQUE
);

CREATE TABLE Course (
    id     INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    title  TEXT UNIQUE
);

CREATE TABLE Member (
    user_id     INTEGER,
    course_id   INTEGER,
    role        INTEGER,
    PRIMARY KEY (user_id, course_id)
)''')

fname = input('Enter file name: ')
if len(fname) < 1: fname = 'roster_data_sample.json'
file = open(fname).read()
json_data = json.loads(file)

for line in json_data:
    name = line[0]
    title = line[1]
    role = line[2]

    cur.execute('INSERT OR IGNORE INTO User (name) VALUES (?)', (name,))
    cur.execute('SELECT id FROM User WHERE name = ?', (name,))
    user_id = cur.fetchone()[0]

    cur.execute('INSERT OR IGNORE INTO Course (title) VALUES (?)', (title,))
    cur.execute('SELECT id FROM Course WHERE title = ?', (title,))
    course_id = cur.fetchone()[0]

    cur.execute('INSERT OR REPLACE INTO Member (user_id, course_id, role) VALUES (?, ?, ?)', (user_id, course_id, role))

    conn.commit()

sqlstr = '''SELECT User.name, Course.title, Member.role FROM User JOIN Course JOIN Member
            ON Member.user_id = User.id AND Member.course_id = Course.id
            ORDER BY Course.title, Member.role DESC, User.name'''

for row in cur.execute(sqlstr):
    print('User:', str(row[0]), '\nCourse:', str(row[1]), '\nRole:', row[2], '\n')

cur.close()