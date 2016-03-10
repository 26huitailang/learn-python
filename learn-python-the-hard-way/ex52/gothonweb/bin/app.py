import web
from gothonweb import map
from random import randint

urls = (
  '/game', 'GameEngine',
  '/', 'Index',
)

app = web.application(urls, globals())

# little hack so that debug mode works with sessions
if web.config.get('_session') is None:
    store = web.session.DiskStore('sessions')
    session = web.session.Session(app, store,
                                  initializer={'room': map.START, 'guesses': 0})
    web.config._session = session
else:
    session = web.config._session

render = web.template.render('templates/', base="layout")

class Index(object):
    def GET(self):
        # this is used to "setup" the session with starting values
        session.room = map.START
        web.seeother("/game")

class GameEngine(object):


    def GET(self):
        if session.room:
            if session.room.name == "death":
                return render.you_died(quip=map.quips[randint(0, len(map.quips)-1)])
            # elif session.room.name == "Laser Weapon Armory":

            else:
                return render.show_room(room=session.room, nums=10-session.guesses)
        else:
            # why is there here? do you need it? catch the wrong input
            return render.you_died(quip=map.quips[randint(0, len(map.quips)-1)])

    def POST(self):
        form = web.input()

        # there is a bug here, can you fix it?
        if session.room and form.action:
            try:
                int(form.action)
                if session.room.name == "Laser Weapon Armory":
                    # guesses = 0
                    while (form.action != map.code) and (session.guesses < 10):
                        print "BZZZZEDDD!"
                        print session.guesses
                        session.guesses += 1
                        web.seeother("/game")
                        # form = web.input()
                        # guess = raw_input("[keypad]> ")
                    # if form.action == map.code:
                    #     session.room = session.room.go(form.action)
            except ValueError:
                session.room = session.room.go(form.action)
                web.seeother("/game")

if __name__ == "__main__":

    app.run()