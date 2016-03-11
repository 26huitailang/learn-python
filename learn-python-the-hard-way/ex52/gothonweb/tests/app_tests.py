from nose.tools import *
from bin import app
from tests.tools import assert_response
import web
from gothonweb import map

# def test_Index():
#     # check that we get a 404 on the / URL
#     resp = app.request("/aaa")
#     assert_response(resp, status="404")
#
#     # test our first GET request to /hello
#     resp = app.request("/")
#     assert_response(resp)

# @with_setup(setUp())
class test_GameEngine():
    if web.config.get('_session') is None:
        store = web.session.DiskStore('sessions')
        session = web.session.Session(app, store,
                                      initializer={'room': None, 'guesses': 0})
        web.config._session = session
    else:
        session = web.config._session

    game = app.GameEngine()

    def setUp(self):
        self.session.room = map.START
        self.session.guesses = 0
        print "set up!"

    def tearDown(self):
        # print session.room.name
        # session.room = map.START
        print "tear down!"


    def test_GET(self):
        # make sure default values work for the form
        # resp = self.game.GET()
        resp = app.app.request("/game", method="GET")
        # print resp
        assert_response(resp, contains=None)


    def test_POST(self):
        # test that we get expected values
        data = {'action': 'tell a joke'}
        resp1 = app.app.request("/")
        # print self.session.room.name
        resp2 = app.app.request("/game", method="GET")
        assert_response(resp2, contains="Central Corridor")
        resp3 = app.app.request("/game", method="POST", data=data)
        resp = app.app.request("/game", method="GET")
        print resp1
        # resp = app.app.request("/", method="GET")
        print resp2
        print resp
        # resp2 = aapp.session.get('room')
        # print resp2
        # assert_equal(resp, laser_weapon_armory)
        # resp = app.request("/game", method="GET")
        assert_response(resp, contains="Laser Weapon Armory")
