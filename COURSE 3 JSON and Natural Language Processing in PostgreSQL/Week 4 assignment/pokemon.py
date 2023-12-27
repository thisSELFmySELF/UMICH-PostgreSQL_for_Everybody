# To retrieve only the urls that start with 1 and end with 100
# Get the data and insert it into the body column in postgresql
import psycopg2
import hidden
import myutils
import requests
import json

# Load the secrets
secrets = hidden.secrets()
conn = psycopg2.connect(host=secrets['host'],
        port=secrets['port'],
        database=secrets['database'],
        user=secrets['user'],
        password=secrets['pass'],
        connect_timeout=3)

cur = conn.cursor()

print('DROP TABLE IF EXISTS pokeapi CASCADE;')
print(' ')

sql = '''
CREATE TABLE IF NOT EXISTS pokeapi (id INTEGER, body JSONB);
'''
print(sql)
cur.execute(sql)

for i in range(1,101):
    url = 'https://pokeapi.co/api/v2/pokemon/'+ str(i)
    r = requests.get(url)
    js = json.loads(r.text)
    json_object = json.dumps(js, indent = 4)
    sql = 'INSERT INTO pokeapi (body) VALUES (%s);'
    cur.execute(sql, ([json_object,]))

conn.commit()
cur.close()
