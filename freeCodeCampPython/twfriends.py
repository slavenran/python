import urllib.request, urllib.parse, urllib.error
import twurl
import json
import sqlite3
import ssl

TWITTER_URL = 'https://api.twitter.com/1.1/friends/list.json'

conn = sqlite3.connect('friends.sqlite')
cur = conn.cursor()

# kreiranje tabela
cur.execute('''
            CREATE TABLE IF NOT EXISTS People
            (id INTEGER PRIMARY KEY, name TEXT UNIQUE, retrieved INTEGER)''')
cur.execute('''
            CREATE TABLE IF NOT EXISTS Follows
            (from_id INTEGER, to_id INTEGER, UNIQUE(from_id, to_id))''')

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    acct = input('Enter a twitter account, or quit: ')
    if acct == 'quit': break
    # bira random akaunt koji je 0 puta bio retrievovan i dodaje njegov id i name u konstante
    if len(acct) < 1:
        cur.execute('SELECT id, name FROM People WHERE retrieved = 0 LIMIT 1')
        try:
            id, acct = cur.fetchone()
        except:
            print('No unretrieved Twitter accounts found')
            continue
    else:      # trazi da li ima osoba sa tim imenom u bazi
        cur.execute('SELECT id FROM People WHERE name = ? LIMIT 1', (acct, ))
        try:        # uzima id te osobe
            id = cur.fetchone()[0]
        except:     # ako nema onda ubacuje ime u bazu i uzima njen novi autoinkrementovani id da ubaci u konstantu
            cur.execute('INSERT OR IGNORE INTO People (name, retrieved) VALUES (?, 0)', (acct, ))
            conn.commit()
            if cur.rowcount != 1:
                print('Error inserting account:', acct)
                continue
            id = cur.lastrowid
    # pokretanje konekcije
    url = twurl.augment(TWITTER_URL, {'screen_name': acct, 'count': '100'})
    print('Retrieving', acct)
    try:
        connection = urllib.request.urlopen(url, context=ctx)
    except Exception as err:
        print('Failed due to too many requests', err)
        quit()
    data = connection.read().decode()
    headers = dict(connection.getheaders())

    print('Remaining', headers['x-rate-limit-remaining'])

    try:
        js = json.loads(data)
    except:
        print('Unable to parse json')
        print(data)
        break

    if 'users' not in js:
        print('Incorrect JSON recieved')
        print(json.dumps(js, indent=4))
        continue

    # apdejtuje retrieved value unesene osobe (bilo da je tek napravljena ili vec bila u bazi)
    cur.execute('UPDATE People SET retrieved = 1 WHERE name = ?', (acct, ))

    countnew = 0
    countold = 0
    for u in js['users']:
        friend = u['screen_name']
        print(friend)
        # gleda da li prijatelj vec postoji unutar baze
        cur.execute('SELECT id FROM People WHERE name = ? LIMIT 1', (friend, ))
        try:
            # ako postoji uzima mu id da bi mogao napraviti konekciju
            friend_id = cur.fetchone()[0]
            countold += 1
        except:
            # ako ne postoji pravi ga u bazi
            cur.execute('INSERT OR IGNORE INTO People (name, retrieved) VALUES (?, 0)', (friend, ))
            conn.commit()
            if cur.rowcount != 1:
                print('Error inserting account:', friend)
                continue
            friend_id = cur.lastrowid
            countnew += 1
        # nova follow konekcija u bilo kojem slucaju
        cur.execute('INSERT OR IGNORE INTO Follows (from_id, to_id) VALUES (?, ?)', (id, friend_id))
    print('New accounts=', countnew, ' revisited=', countold)
    conn.commit()

print('Remaining', headers['x-rate-limit-remaining'])
cur.close()