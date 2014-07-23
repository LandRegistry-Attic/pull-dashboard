from flask import render_template
from pulldashboard import app
from models import PullRequest
from pulldashboard import excludedRepos
import requests
import time
from calendar import timegm

@app.route('/')
def index():
    url = app.config['GITHUB_API_ISSUES_URL']

    pulls = []

    # Required headers for a GET request
    r = requests.get(url, headers=app.config['GITHUB_API_HEADERS'])
    if r.status_code == requests.codes.ok:
        raw_issues = r.json()
        for raw_issue in raw_issues:
            # Check blacklist
            if raw_issue['repository']['full_name'] in excludedRepos:
                break

            # Check if issue is actually a pull request
            if 'pull_request' in raw_issue:

                print raw_issue
                pr = PullRequest(raw_issue['number'], raw_issue['title'], raw_issue['user']['login'], timegm(time.strptime(raw_issue['created_at'].replace('Z', 'GMT'), '%Y-%m-%dT%H:%M:%S%Z')), raw_issue['repository']['name'])


                pulls.append(pr)

    # Sort by time
    pulls.sort(key=lambda x: x.created_at, reverse=False)

    return render_template("index.html", pulls=pulls)

#  Some useful headers to set to beef up the robustness of the app
# https://www.owasp.org/index.php/List_of_useful_HTTP_headers
@app.after_request
def after_request(response):
    response.headers.add('Content-Security-Policy', "default-src 'self' 'unsafe-inline' data:")
    response.headers.add('X-Frame-Options', 'deny')
    response.headers.add('X-Content-Type-Options', 'nosniff')
    response.headers.add('X-XSS-Protection', '1; mode=block')
    return response
