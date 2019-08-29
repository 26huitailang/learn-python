import pytest
import smtplib
import tempfile
import os


@pytest.fixture(scope='module', params=["smtp.gmail.com", "mail.python.org"])
def smtp(request):
    smtp = smtplib.SMTP(request.param)
    yield smtp
    print("finalizing %s" % smtp)
    smtp.close()


@pytest.fixture
def cleandir():
    newpath = tempfile.mkdtemp()
    os.chdir(newpath)


@pytest.fixture
def transact(self, request, db):
    db.begin()
    yield
    db.rollback()


@pytest.fixture
def username():
    return 'username'
