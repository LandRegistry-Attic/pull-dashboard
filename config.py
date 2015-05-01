import os

# Get things from environment
settings = os.environ.get('SETTINGS')
github_api_key = os.environ.get('GITHUB_API_KEY')
jenkins_host = os.environ.get('JENKINS_HOST')
jenkins_user = os.environ.get('JENKINS_USER')
jenkins_password = os.environ.get('JENKINS_PASSWORD')

# The config dict to be used in public
CONFIG_DICT = {
    'DEBUG': False,
    'REPOSITORY_BLACKLIST': 'Blacklistfile',
    'GITHUB_API_ISSUES_URL': "https://api.github.com/orgs/LandRegistry/issues",
    # split parameter out so URL config var can be used for response mocking
    'GITHUB_API_ISSUES_FILTER': "?filter=all",
    'GITHUB_API_HEADERS': {
        'User-Agent': 'LandRegistry-Build-Dashboard/1.0.0',
        'Accept': 'application/vnd.github.v3+json',
        'Content-type': 'application/json',
        'Authorization': 'token {}'.format(github_api_key)
    },
    'JENKINS_URL': jenkins_host + '/api/json?pretty=true&depth=2&&tree=jobs[name,buildable,lastBuild[number,duration,timestamp,culprits[fullName],result,url,changeSet[items[msg,author[fullName]]]]]',
    'JENKINS_USER': jenkins_user,
    'JENKINS_PASSWORD': jenkins_password
}


# Make further tweaks based on environment
if settings == 'dev':
    CONFIG_DICT['DEBUG'] = True
elif settings == 'test':
    CONFIG_DICT['LOGGING'] = False
    CONFIG_DICT['DEBUG'] = True
    CONFIG_DICT['TESTING'] = True
