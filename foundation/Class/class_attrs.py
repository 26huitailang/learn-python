import attr

@attr.s
class Person(object):
    name = attr.ib()
    age = attr.ib()
    salary = attr.ib()
    job = attr.ib()

if __name__ == "__main__":
    p = Person('peter', 18, 0, 'worker')
    print(p)
    print(attr.asdict(p))
    print(attr.asdict(p, filter=lambda a, v: a.name in ('name', 'age')))
