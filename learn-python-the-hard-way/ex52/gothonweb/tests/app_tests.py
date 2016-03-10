from nose.tools import *
from bin.app import app
from tests.tools import assert_response
from bin import app as aapp

def setUp():
    pass


def test_Index():
    # check that we get a 404 on the / URL
    resp = app.request("/aaa")
    assert_response(resp, status="404")

    # test our first GET request to /hello
    resp = app.request("/")
    assert_response(resp)

@with_setup(setUp())
def test_GameEngine():

    # make sure default values work for the form
    resp = app.request("/game", method="GET")
    assert_response(resp, contains="Central Corridor")

def test_POST():
    # test that we get expected values
    data = {'action': 'tell a joke'}
    resp = app.request("/game", method="POST", data=data)
    print resp
    resp2 = aapp.session.get('room')
    print resp2
    # assert_equal(resp, laser_weapon_armory)
    # resp = app.request("/game", method="GET")
    # assert_response(resp, contains="Laser Weapon Armory")
