# class对象实现json的转换
import json


class Person(object):
    def __init__(self, name: str, age: int, salary: int, job: str):
        self.name = name
        self.age = age
        self.salary = salary
        self.job = job

    def to_json(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)


if __name__ == "__main__":
    p = Person('peter', 22, 0, 'worker')
    print(p.to_json())