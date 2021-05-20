import urllib.request, urllib.parse, urllib.error
import twurl
import json
import ssl

TWITTER_URL = 'https://api.twitter.com/1.1/statuses/user_timeline.json'

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    print()
    acct = input('Enter Twitter Account:')
    if(len(acct) < 1): break
    url = twurl.augment(TWITTER_URL, {'screen_name': acct, 'count': '5'})
    print('Retrieving', url)
    connection = urllib.request.urlopen(url, context=ctx)
    data = connection.read().decode()
    headers = dict(connection.getheaders())
    print('Remaining', headers['x-rate-limit-remaining'])
    js = json.loads(data)
    # print(json.dumps(js, indent=4))

    for u in js:
        print(u['user']['screen_name'])
        if 'description' not in u['user']:
            print('  No status found')
            continue
        s = u['user']['description']
        print('  ', s[:50])