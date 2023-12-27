import psycopg2
import hidden

secrets = hidden.secrets()

conn = psycopg2.connect(host=secrets['host'],
        port=secrets['port'],
        database=secrets['database'],
        user=secrets['user'],
        password=secrets['pass'],
        connect_timeout=3)

cur = conn.cursor()

sql = 'DROP TABLE IF EXISTS pythonseq CASCADE;'
print(sql)
cur.execute(sql)

sql = 'CREATE TABLE pythonseq (iter INTEGER, val INTEGER);'
print(sql)
cur.execute(sql)

conn.commit()    # Flush it all to the DB server

iter = 1
val = 455196
sql = 'INSERT INTO pythonseq (iter, val) VALUES (%s, %s);'
cur.execute(sql, (iter,val))
conn.commit()

val = 455196
for i in range(1,300) :
    iter = i+1
    print(iter, val)
    val = int((val * 22) / 7) % 1000000

    sql = 'INSERT INTO pythonseq (iter, val) VALUES (%s, %s);'
    cur.execute(sql, (iter,val))

conn.commit()
cur.close()
