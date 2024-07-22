import sqlite3

conn = sqlite3.connect(r'manyToMany.sqlite')
cur = conn.cursor()

cur.executescript(
    ''' 
    DROP TABLE IF EXISTS User;
    DROP TABLE IF EXISTS Course;
    DROP TABLE IF EXISTS Member;

    CREATE TABLE User (
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
        name TEXT,
        email TEXT
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

# Insertar valores
cur.executescript(
    '''
    INSERT INTO User (name, email) VALUES ('Jane', 'jane@tsugi.org');
    INSERT INTO User (name, email) VALUES ('Ed', 'ed@tsugi.org');
    INSERT INTO User (name, email) VALUES ('Sue', 'sue@tsugi.org');
    
    INSERT INTO Course (title) VALUES ('Python');
    INSERT INTO Course (title) VALUES ('SQL');
    INSERT INTO Course (title) VALUES ('PHP');
    '''
)

# Insertar valores a la tabla mucho a muchos
cur.executescript(
    '''
    INSERT INTO Member (user_id, course_id, role) VALUES (1,1,1);
    INSERT INTO Member (user_id, course_id, role) VALUES (2,1,0);
    INSERT INTO Member (user_id, course_id, role) VALUES (3,1,0);
    INSERT INTO Member (user_id, course_id, role) VALUES (1,2,0);
    INSERT INTO Member (user_id, course_id, role) VALUES (2,2,1);
    INSERT INTO Member (user_id, course_id, role) VALUES (2,3,1);
    INSERT INTO Member (user_id, course_id, role) VALUES (3,3,0);
    '''
)

# Crear reporte de Usuario esta registrado en curso
cur.execute(
    '''
    SELECT User.name, Member.role, Course.title
    FROM User JOIN Member JOIN Course
    ON Member.user_id = User.id AND Member.course_id = Course.id
    ORDER BY Course.title, Member.role DESC, User.name
    '''
)

