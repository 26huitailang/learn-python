from nose.tools import *
from bin.app import app
from tests.tools import assert_response
import web


def test_Index():
    # check that we get a 404 on the / URL

    resp = app.request("/re")
    print "resp, index:", resp
    assert_response(resp, status="404")

    # test our first GET request to /hello
    resp = app.request("/")
    web.ctx.session.save()
    assert_response(resp, status='303')

def test_GameEngine():
    # make sure default values work for the form
    session = web.config._session
    # web.header('Set-Cookie', 'webpy_session_id=10a98447e9a79d19513226ea79aed7b2801ee6df; Path=/; httponly')
    resp = app.request("/", method="GET") #, headers={'Ser-Cookie': 'webpy_session_id=10a98447e9a79d19513226ea79aed7b2801ee6df; Path=/; httponly'}
    assert_response(resp, contains="Central Corridor")

    # test that we get expected values
    data = {'name': 'Zed', 'greet': 'Hola'}
    resp = app.request("/hello", method="POST", data=data)
    assert_response(resp, contains="Zeed")