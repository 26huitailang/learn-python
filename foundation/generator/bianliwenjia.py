import os


def tree(top):
    for path, names, fnames in os.walk(top):
        for fname in fnames:
            yield os.path.join(path, fname)


for name in tree('d:\git-checkout\Flaskr'):
    print(name)
