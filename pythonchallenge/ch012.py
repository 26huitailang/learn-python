# content=open("evil2.gfx").read()  
# [open("12_%d.jpg" %i, "w").write(content[i::5]) for i in range(5)]

import Image
from cStringIO import StringIO

s = open("evil2.gfx", "rb").read()
for i in range(5):
    piece = s[i::5]  # every fifth byte, starting at i
    im = Image.open(StringIO(piece))
    f = open("%d.%s" % (i, im.format.lower()), "wb")
    f.write(piece)
    f.close()

