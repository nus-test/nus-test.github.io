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
'dbms' : 'Database Management Systems',
'datalog' : 'Datalog Engines',
'xml' : 'XML Processors',
'compiler&interpreter': 'Compilers and Interpreters'
}


common_where_clause = "(resolution IN ('confirmed', 'fixed', 'open') OR resolution IS NULL)"
domain_count_query = 'SELECT domain, COUNT(*) FROM bugs WHERE ' + common_where_clause + ' GROUP BY domain ORDER BY COUNT(*) DESC;'
print('<b>Overview</b><br/>')
print('<ul>')
for domain, count in c.execute(domain_count_query).fetchall():
    print('<li>%s: %d bugs</li>' % (domain_map[domain], count))
print('</ul>')


print('<br/>')
for domain, count in c.execute(domain_count_query).fetchall():
    print('<h2>%s (%d bugs)</h2>' % (domain_map[domain], count))
    for system, count in c.execute(("SELECT system, COUNT(*) FROM bugs WHERE domain = '%s' AND " + common_where_clause + " GROUP BY system ORDER BY COUNT(*) DESC") % (domain,)).fetchall():
        print('<h3>%s (%d bugs)</h3>' % (system, count))
        for title, url, found_by, resolution in c.execute(("SELECT title, url, reported_by, resolution FROM bugs WHERE domain='%s' AND system='%s' AND " + common_where_clause + ";") % (domain, system)).fetchall():
            print('<details>')
            print('<summary>%s</summary>'% (title, ))
            if resolution is None:
                resolution = 'unconfirmed'
            print('Status: %s<br />' % (resolution, ))
            print('Link: <a href="%s">%s</a> <br />' % (url, url))
            print('Found by: %s' % (found_by,))
            print('</details>')
