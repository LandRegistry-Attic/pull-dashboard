from datetime import datetime
class PullRequest(object):
    def __init__(self, number, title, user, created_at, repo_name):
        self.number = number
        self.title = title
        self.user = user
        self.created_at = created_at
        self.repo_name = repo_name

		# Determine how old the record is
        now = datetime.now()
    	then = datetime.fromtimestamp(self.created_at)
    	tdelta = now - then
        self.days_old = tdelta.days;
        self.hours_old = tdelta.seconds // 3600;


    def getCleanCreatedAt(self):
        return datetime.fromtimestamp(self.created_at).strftime('%Y-%m-%d %H:%M:%S')
