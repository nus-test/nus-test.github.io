import json
from collections import Counter
from html import escape

with open("data/bugs.json") as f:
    data = json.load(f)

domain_map = {
'dbms' : 'Database Management Systems',
'datalog' : 'Datalog Engines',
'xml' : 'XML Processors',
'compiler&interpreter': 'Compilers and Interpreters'
}

def is_included(entry):
    return entry.get('resolution') in ('confirmed', 'fixed', 'open', None)


included_bugs = [entry for entry in data if is_included(entry)]
domain_counts = Counter(entry.get('domain') for entry in included_bugs)
ordered_domains = sorted(domain_counts.items(), key=lambda item: item[1], reverse=True)

print('<b>Overview</b><br/>')
print('<ul>')
for domain, count in ordered_domains:
    print('<a href="#%s"><li>%s: %d bugs</li></a>' % (domain, domain_map[domain], count))
print('</ul>')

print('''
<div class="bug-database-controls">
<button type="button" class="expand-bug-databases">Expand all databases</button>
<button type="button" class="collapse-bug-databases">Collapse all databases</button>
</div>
<style>
.bug-database-controls {
  display: flex;
  gap: 0.6rem;
  margin: 1rem 0;
  flex-wrap: wrap;
}

.bug-database-controls button {
  padding: 0.4rem 0.8rem;
  border: 1px solid #1565c0;
  border-radius: 4px;
  color: #1565c0;
  background: transparent;
  cursor: pointer;
}

.bug-database-controls button:hover {
  color: #fff;
  background: #1565c0;
}

.bug-database-group {
  margin: 0.8rem 0;
  border: 1px solid rgba(0, 0, 0, 0.12);
  border-radius: 4px;
}

.bug-database-group > summary {
  padding: 0.7rem 1rem;
  cursor: pointer;
  font-size: 1.15rem;
  font-weight: 600;
}

.bug-database-group[open] > summary {
  border-bottom: 1px solid rgba(0, 0, 0, 0.12);
}

.bug-database-group > .bug-entry {
  margin: 0.7rem 1rem;
}
</style>
''')

print('<br/>')
for domain, count in ordered_domains:
    print('<h2 id="%s">%s (%d bugs)</h2>' % (domain, domain_map[domain], count))
    domain_bugs = [entry for entry in included_bugs if entry.get('domain') == domain]
    system_counts = Counter(entry.get('system') for entry in domain_bugs)
    ordered_systems = sorted(system_counts.items(), key=lambda item: item[1], reverse=True)
    for system, count in ordered_systems:
        print('<details class="bug-database-group">')
        print('<summary>%s (%d bugs)</summary>' % (escape(system or 'Unknown database'), count))
        for entry in domain_bugs:
            if entry.get('system') != system:
                continue
            title = entry.get('title')
            url = entry.get('url')
            found_by = entry.get('reported_by')
            resolution = entry.get('resolution')
            print('<details class="bug-entry">')
            print('<summary>%s</summary>' % escape(title or 'Untitled bug'))
            if resolution is None:
                resolution = 'unconfirmed'
            safe_url = escape(url or '', quote=True)
            print('Status: %s<br />' % escape(resolution))
            print('Link: <a href="%s">%s</a> <br />' % (safe_url, escape(url or '')))
            print('Found by: %s' % escape(found_by or 'Unknown'))
            print('</details>')
        print('</details>')

print('''
<script>
document.addEventListener('DOMContentLoaded', function() {
  var groups = Array.prototype.slice.call(document.querySelectorAll('.bug-database-group'));
  var expandButton = document.querySelector('.expand-bug-databases');
  var collapseButton = document.querySelector('.collapse-bug-databases');
  if (!groups.length) return;

  expandButton.addEventListener('click', function() {
    groups.forEach(function(group) { group.open = true; });
  });

  collapseButton.addEventListener('click', function() {
    groups.forEach(function(group) { group.open = false; });
  });
});
</script>''')
