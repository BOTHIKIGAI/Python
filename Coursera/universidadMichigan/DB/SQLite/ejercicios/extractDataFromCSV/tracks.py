import sqlite3

conn = sqlite3.connect(r'db3SQLite.db') # se conecta a la base de datos por medio de la libreria y el metodo connect
cur = conn.cursor() # invoca al metodo cursor que nos provee un objeto para la ejecución de scripts

# Se ejecuta el siguiente script
cur.executescript('''
DROP TABLE IF EXISTS Artist;
DROP TABLE IF EXISTS Album;
DROP TABLE IF EXISTS Track;

CREATE TABLE Artist (
    id  INTEGER PRIMARY KEY,
    name    TEXT UNIQUE
);

CREATE TABLE Album (
    id  INTEGER PRIMARY KEY,
    artist_id  INTEGER,
    title   TEXT UNIQUE
);

CREATE TABLE Track (
    id  INTEGER PRIMARY KEY,
    title TEXT  UNIQUE,
    album_id  INTEGER,
    len INTEGER, rating INTEGER, count INTEGER
);
''')

handle = open('tracks.csv') # abre el archivo csv

# Another One Bites The Dust,Queen,Greatest Hits,55,100,217103
#   0                          1      2           3  4   5

for line in handle: # itera linea por linea
    line = line.strip(); # elimina los espacios en blancos
    pieces = line.split(',') # Divide la linea (string) por las comas que los separan
    if len(pieces) < 6 : continue # Si la cantidad de elementos de pieces es menor a 6 continuara

    # Si la lista es mayor o igual realizara todo lo demas, tomando elemento por elemento
    name = pieces[0]
    artist = pieces[1]
    album = pieces[2]
    count = pieces[3]
    rating = pieces[4]
    length = pieces[5]

    # COMENZARA A INSERTAR Y EXTRAER EL ID 
    cur.execute('''INSERT OR IGNORE INTO Artist (name) 
        VALUES ( ? )''', ( artist, ) )
    cur.execute('SELECT id FROM Artist WHERE name = ? ', (artist, ))
    artist_id = cur.fetchone()[0]

    cur.execute('''INSERT OR IGNORE INTO Album (title, artist_id) 
        VALUES ( ?, ? )''', ( album, artist_id ) )
    cur.execute('SELECT id FROM Album WHERE title = ? ', (album, ))
    album_id = cur.fetchone()[0]

    cur.execute('''INSERT OR REPLACE INTO Track
        (title, album_id, len, rating, count) 
        VALUES ( ?, ?, ?, ?, ? )''', 
        ( name, album_id, length, rating, count ) )

    conn.commit()
