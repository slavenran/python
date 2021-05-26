import urllib.request
import twurl
import json
import sqlite3
import ssl

TWITTER_URL = 'https://api.twitter.com/1.1/friends/list.json'

conn = sqlite3.connect('mytwitterfriends.sqlite')
cur = conn.cursor()

cur.execute('CREATE TABLE IF NOT EXISTS Accounts (id INTEGER PRIMARY KEY, name TEXT UNIQUE, retrieved INTEGER)')
cur.execute('CREATE TABLE IF NOT EXISTS Following (id INTEGER, follows_id INTEGER, UNIQUE (id, follows_id))')

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    acct = input('Enter a twitter account or quit: ')
    if acct == 'quit': break
    if len(acct) < 1:
        cur.execute('SELECT id, name FROM Accounts WHERE retrieved = 0 LIMIT 1')
        try:
            id, acct = cur.fetchone()
        except:
            print('No unretrieved accounts found')
            continue
    else:
        cur.execute('SELECT id FROM Accounts WHERE name = ? ', (acct, ))
        try:
            id = cur.fetchone()[0]
        except:
            cur.execute('INSERT OR IGNORE INTO Accounts (name, retrieved) VALUES (?, 0)', (acct, ))
            conn.commit()
            if cur.rowcount != 1:
                print('Error inserting new user')
                continue
            id = cur.lastrowid
    
    url = twurl.augment(TWITTER_URL, {'screen_name':acct, 'count':'100'})
    connection = urllib.request.urlopen(url, context=ctx)
    data = connection.read().decode()
    headers = dict(connection.getheaders())
    print('Remaining:', headers['x-rate-limit-remaining'])

    js = json.loads(data)

    cur.execute('UPDATE Accounts SET retrieved = 1 WHERE name = ? ', (acct, ))

    for u in js['users']:
        following = u['screen_name']
        print(following)
        cur.execute('SELECT id FROM Accounts WHERE name = ? ', (following, ))
        try:
            following_id = cur.fetchone()[0]
        except:
            cur.execute('INSERT OR IGNORE INTO Accounts (name, retrieved) VALUES (?, 0)', (following, ))
            conn.commit()
            if cur.rowcount != 1:
                print('Error while inserting')
                break
            following_id = cur.lastrowid
        cur.execute('INSERT OR IGNORE INTO Following (id, follows_id) VALUES (?, ?)', (id, following_id))
    conn.commit()
    print('Remaining:', headers['x-rate-limit-remaining'])
cur.close()