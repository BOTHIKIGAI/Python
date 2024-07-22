# 1. importar sqlite3
import sqlite3

# 2. Establecer conexión y ejecución de script
conn = sqlite3.connect(r'db4SQLite.sqlite')
cur = conn.cursor()

# 3. Crear tablas de la base de datos
cur.executescript(
    '''
    DROP TABLE IF EXISTS Artist;
    DROP TABLE IF EXISTS Genre;
    DROP TABLE IF EXISTS Album;
    DROP TABLE IF EXISTS Track;

    CREATE TABLE Artist (
        id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
        name    TEXT UNIQUE
    );

    CREATE TABLE Genre (
        id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
        name    TEXT UNIQUE
    );

    CREATE TABLE Album (
        id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
        artist_id  INTEGER,
        title   TEXT UNIQUE
    );

    CREATE TABLE Track (
        id  INTEGER NOT NULL PRIMARY KEY 
            AUTOINCREMENT UNIQUE,
        title TEXT  UNIQUE,
        album_id  INTEGER,
        genre_id  INTEGER,
        len INTEGER,
        rating INTEGER,
        count INTEGER
    );
    '''
)

# 4. Abrir archivo
fhand = open('tracks.csv')

# 5. Recorrer linea por linea
for line in fhand:
    line = line.strip() # 5.1 Eliminar espacios en blanco
    line = line.split(',') # 5.2 Dividir la linea por comas = ['Another One Bites The Dust', 'Queen', 'Greatest Hits', '55', '100', '217103', 'Rock']
    if len(line) < 6: continue

    name = line[0]
    artist = line[1]
    album = line[2]
    count = line[3]
    rating = line[4]
    length = line[5]
    gener = line[6]

    # 5.3 Artist
    cur.execute('''INSERT OR IGNORE INTO Artist (name) VALUES ( ? )''', ( artist, ) )
    cur.execute('SELECT id FROM Artist WHERE name = ? ', (artist, ))
    artist_id = cur.fetchone()[0]

    # 5.4 Gener
    cur.execute( ''' INSERT OR IGNORE INTO Genre (name) VALUES (?) ''', ( gener, ))
    cur.execute('SELECT id FROM Genre WHERE name = ? ', (gener, ))
    gener_id = cur.fetchone()[0]

    # 5.5 Album
    cur.execute( ''' INSERT OR IGNORE INTO Album (artist_id, title) VALUES (?, ?) ''', ( artist_id, album, ))
    cur.execute('SELECT id FROM Album WHERE title = ? ', (album, ))
    album_id = cur.fetchone()[0]

    # 5.6 Track
    cur.execute( ' INSERT OR IGNORE INTO Track ( title, album_id, genre_id, len, rating, count ) VALUES ( ?, ?, ?, ?, ?, ? ) ', ( name, album_id, gener_id, length, rating, count, ) )

# . Finalizar conexión
conn.commit()
