# coding: utf-8
from pprint import pprint

attributes = ["name", "dob", "gender"]
values = [
    ["jason", "2000-01-01", "male"],
    ["mike", "1999-01-01", "male"],
    ["nancy", "2001-02-01", "female"],
]


def one_line():
    return [dict(zip(attributes, x)) for x in values]


pprint(one_line())


def loop():
    ret = []
    for v in values:
        tmp = {}
        for i in range(0, len(v)):
            tmp[attributes[i]] = v[i]
        ret.append(tmp)
    return ret


pprint(loop())
# expected outout:
print("expected:\n")
pprint(
    [
        {"name": "jason", "dob": "2000-01-01", "gender": "male"},
        {"name": "mike", "dob": "1999-01-01", "gender": "male"},
        {"name": "nancy", "dob": "2001-02-01", "gender": "female"},
    ]
)
