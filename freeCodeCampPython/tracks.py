from os import truncate
import xml.etree.ElementTree as ET
import sqlite3

conn = sqlite3.connect('trackdb.sqlite')
cur = conn.cursor()

cur.executescript('''
DROP TABLE IF EXISTS Artist;
DROP TABLE IF EXISTS Album;
DROP TABLE IF EXISTS Track;

CREATE TABLE Artist (
    id  INTEGER NOT NULL PRIMARY KEY UNIQUE,
    name    TEXT UNIQUE
);

CREATE TABLE Album (
    id  INTEGER NOT NULL PRIMARY KEY UNIQUE,
    artist_id  INTEGER,
    title   TEXT UNIQUE
);

CREATE TABLE Track (
    id  INTEGER NOT NULL PRIMARY KEY 
        AUTOINCREMENT UNIQUE,
    title TEXT  UNIQUE,
    album_id  INTEGER,
    len INTEGER, rating INTEGER, count INTEGER
);''')

def lookup(d, key):
    found = False
    for child in d:
        if found is True:               # it takes the next element after the key, which is value
            return child.text
        if child.tag == 'key' and child.text == key:
            found = True
    return None

filename = input('Enter file name: ')
if len(filename) < 1: filename = 'Library.xml'
xml_file = ET.parse(filename)
for line in xml_file.findall('dict/dict/dict'):

    if lookup(line, 'Track ID') is None: continue

    track_title = lookup(line, 'Name')
    name = lookup(line, 'Artist')
    album_title = lookup(line, 'Album')
    track_len = lookup(line, 'Total Time')
    rating = lookup(line, 'Rating')
    count = lookup(line, 'Play Count')

    if album_title is None or name is None: continue

    # print(track_title, name, album_title)

    # data = line.findall('string')                             my failed attemp to do this
    # print(data[0].text, data[1].text, data[3].text)
    # track_title = data[0].text
    # name = data[1].text
    # album_title = data[3].text
    cur.execute('INSERT OR IGNORE INTO Artist (name) VALUES (?)', (name, ))
    cur.execute('SELECT id FROM Artist WHERE name = ? ', (name, ))
    artist_id = cur.fetchone()[0]
    # print(artist_id)

    cur.execute('INSERT OR IGNORE INTO Album (artist_id, title) VALUES (?, ?)', (artist_id, album_title))
    cur.execute('SELECT id FROM Album WHERE title = ? ', (album_title, ))
    album_id = cur.fetchone()[0]

    cur.execute('''INSERT OR IGNORE INTO Track (title, album_id, len, rating, count) 
                VALUES (?, ?, ?, ?, ?)''', (track_title, album_id, track_len, rating, count))
    cur.execute('SELECT id FROM Track WHERE title = ? ', (track_title, ))
    
    conn.commit()

strlen = '''SELECT Track.title, Album.title as album, Artist.name, (Track.len/3600) || ':' || strftime('%M:%S', Track.len/86400.0) as 'total time', Track.rating, Track.count
FROM Track JOIN Album JOIN Artist
ON Track.album_id = Album.id AND Album.artist_id = Artist.id'''

for row in cur.execute(strlen):
    print(row)