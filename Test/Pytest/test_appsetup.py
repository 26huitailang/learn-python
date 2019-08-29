# content of test_appsetup.py

import pytest


class App(object):
    def __init__(self, smtp):
        self.smtp = smtp


@pytest.fixture(scope="module")
def app(smtp):
    return App(smtp)


def test_smtp_exists(app):
    assert app.smtp
