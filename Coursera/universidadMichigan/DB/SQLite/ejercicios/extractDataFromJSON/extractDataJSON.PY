# Importar librerias
import json, sqlite3

conn = sqlite3.connect(r'jsonSQLite.sqlite')
cur = conn.cursor()
fhan = open('roster_data.json').read()
json = json.loads(fhan)

cur.executescript(
    ''' 
    DROP TABLE IF EXISTS User;
    DROP TABLE IF EXISTS Course;
    DROP TABLE IF EXISTS Member;

    CREATE TABLE User (
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
        name TEXT
    );

    CREATE TABLE Course (
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
        title TEXT
    );

    CREATE TABLE Member (
        user_id INTEGER,
        course_id INTEGER,
        role INTEGER,
        PRIMARY KEY (user_id, course_id),
        FOREIGN KEY (user_id) REFERENCES User(id),
        FOREIGN KEY (course_id) REFERENCES Course(id)
    );
    '''
)

for element in json:

    name = element[0]
    course = element[1]
    role = element[2]
    
    # USER
    cur.execute('INSERT OR IGNORE INTO User ( name ) VALUES ( ? )', ( name, ))
    cur.execute('SELECT id FROM User WHERE name = ( ? )', ( name, ))
    user_id = cur.fetchone()[0]

    # Course
    cur.execute('INSERT OR IGNORE INTO Course ( title ) VALUES ( ? )', ( course, ))
    cur.execute('SELECT id FROM Course WHERE title = ( ? )', ( course, ))
    course_id = cur.fetchone()[0]
    
    # Member
    cur.execute('INSERT OR IGNORE INTO Member ( user_id, course_id, role ) VALUES ( ?, ?, ? )', ( user_id, course_id, role ))
    
    
conn.commit()