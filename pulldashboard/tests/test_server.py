import mock
import unittest

from pulldashboard.server import app

class ServerTestCase(unittest.TestCase):
    def is_html(self, r):
        assert r.status_code == 200
        assert r.headers['Content-type'] == 'text/html; charset=utf-8'


    def test_get_home(self):
        client = app.test_client()
        r = client.get('/')
        self.is_html(r)