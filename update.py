import json
import re
import os
from github import Github
import requests
from bs4 import BeautifulSoup
import datetime

f = open("data/bugs.json", "r")
original_content = f.read()
parsed_content = json.loads(original_content)
access_token = os.environ.get('GITHUB_LAB_TOKEN', None)
g = Github(access_token)

def format_date(date):
    return date.strftime("%d/%m/%Y")

repo_to_domain_mapping = {
    'duckdb' : 'dbms',
    'cockroach' : 'dbms',
    'tidb' : 'dbms',
    'souffle' : 'datalog',
    'z3' : 'datalog',
    'cozo' : 'datalog'
}

repo_to_system_mapping = {
    'duckdb' : 'DuckDB',
    'cockroach' : 'CockroachDB',
    'tidb' : 'TiDB',
    'souffle' : 'Soufflé',
    'z3' : 'μZ',
    'cozo' : 'CozoDB'
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
            if 'closed_at' not in entry and issue.closed_at:
                entry['closed_at'] = format_date(issue.closed_at)
            if issue.state: # always update the state
                entry['state'] = issue.state
            if 'domain' not in entry:
                entry['domain'] = repo_to_domain_mapping[repo_name]
            if 'reported_by' not in entry:
                entry['reported_by'] = issue.user.login
            if 'system' not in entry:
                entry['system'] = repo_to_system_mapping[repo_name]
        if entry['url'].startswith('https://sqlite.org/forum/'):
            page = requests.get(entry['url']).content
            soup = BeautifulSoup(page, "html.parser")
            titles = soup.find_all('h1')
            assert titles[0].text == 'SQLite Forum'
            report_title = titles[1].text
            if 'title' not in entry:
                entry['title'] = report_title
            report_title = soup.find('h3', { 'class' : 'forumPostHdr'}).text
            m = re.search('By (.*)\((.*)\) on ([0-9\-]* [0-9:]*)', report_title)
            if m is None: # for some user, there is no full_name
                m = re.search('By (.*)\ on ([0-9\-]* [0-9:]*)', report_title)
                assert m, report_title
                user_name = m.group(1)
                date_reported = datetime.datetime.strptime(m.group(2), '%Y-%m-%d %H:%M:%S')
            else:
                full_name = m.group(1)
                user_name = m.group(2)
                # e.g., 2022-05-11 14:22:28
                date_reported = datetime.datetime.strptime(m.group(3), '%Y-%m-%d %H:%M:%S')
            if 'created_at' not in entry:
                entry['created_at'] = format_date(date_reported)
            if 'reported_by' not in entry:
                entry['reported_by'] = user_name
            if 'domain' not in entry:
                entry['domain'] = 'dbms'
            if 'system' not in entry:
                entry['system'] = 'SQLite'

print(json.dumps(parsed_content, indent=4))
