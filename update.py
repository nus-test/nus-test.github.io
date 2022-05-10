import json
import re
from github import Github


f = open("data/bugs.json", "r")
original_content = f.read()
parsed_content = json.loads(original_content)
g = Github()

def format_date(date):
    return date.strftime("%d/%m/%Y")

repo_to_domain_mapping = {
    'duckdb' : 'dbms'
}

for entry in parsed_content:
    if entry['url']:
        url = entry['url']
        m = re.search("https://github.com/(.*)/(.*)/issues/(.*)", entry['url'])
        if m:
            organization = m.group(1)
            repo_name = m.group(2)
            issue_id = int(m.group(3))
            repo = g.get_repo("%s/%s" % (organization, repo_name))
            issue = repo.get_issue(number=issue_id)
            if 'title' not in entry:
                entry['title'] = issue.title
            if 'created_at' not in entry:
                entry['created_at'] = format_date(issue.created_at)
            if 'closed_at' not in entry:
                entry['fix_date'] = format_date(issue.closed_at)
            if 'state' not in entry:
                entry['state'] = issue.state
            if 'domain' not in entry:
                entry['domain'] = repo_to_domain_mapping[repo_name]
            if 'reported_by' not in entry:
                entry['reported_by'] = issue.user.login

print(json.dumps(parsed_content, indent=4))
