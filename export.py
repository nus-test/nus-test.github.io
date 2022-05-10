import json
import argparse
import sqlite3
import pandas as pd

conn = sqlite3.connect(':memory:')
c = conn.cursor()
with open("data/bugs.json") as f:
    data = json.load(f)

df = pd.DataFrame(data)
df.to_sql('bugs', conn)

domain_map = {
'dbms' : 'Database Management Systems'
}


for (domain,) in c.execute('SELECT DISTINCT domain FROM bugs;').fetchall():
	print('<h2>%s</h2>' % (domain_map[domain], ))
	for title, url, found_by in c.execute("SELECT title, url, reported_by FROM bugs WHERE domain='%s';" % (domain)).fetchall():
		print('<details>')
		print('<summary>%s</summary>'% (title, ))
		print('link: <a href="%s">%s</a> <br />' % (url, url))
		print('found by: %s' % (found_by,))
		print('</details>')
