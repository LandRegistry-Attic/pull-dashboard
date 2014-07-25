import unittest
import responses

from pulldashboard.server import app

class ServerTestCase(unittest.TestCase):

    def is_html(self, r):
        assert r.status_code == 200
        assert r.headers['Content-type'] == 'text/html; charset=utf-8'

    @responses.activate
    def test_get_home_no_results(self):
        client = app.test_client()
        responses.add(responses.GET, app.config['GITHUB_API_ISSUES_URL'],
                  body='[]', status=200,
                  content_type='application/json')

        r = client.get('/')
        self.is_html(r)
        assert len(responses.calls) == 1
        assert responses.calls[0].request.url == app.config['GITHUB_API_ISSUES_URL'] + app.config['GITHUB_API_ISSUES_FILTER']