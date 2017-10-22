# coding: utf-8
from sqlalchemy import func, Column, Integer, String, create_engine, or_, not_
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


db_uri = "sqlite:///:memory:"
engine = create_engine(db_uri, echo=True)

Base = declarative_base()


def init_db():
    Base.metadata.create_all(engine)


def drop_db():
    Base.metadata.drop_all(engine)


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String(30))
    password = Column(String(128))

    def __repr__(self):
        return "<User (name='%s', password='%s')>" % (self.name, self.password)

init_db()

Session = sessionmaker()
Session.configure(bind=engine)
session = Session()

user = User(name='a')
session.add(user)
user = User(name='b')
session.add(user)
user = User(name='a')
session.add(user)
user = User()
session.add(user)
session.commit()
query = session.query(User)
print('1', query) # 显示SQL 语句
count = func.count(User.name)
print('count', count)
print('session.query',session.query(count, User.name).group_by(User.name).all())
