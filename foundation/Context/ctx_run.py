from contextvars import ContextVar, copy_context

var = ContextVar('var')
var.set('spam')

def main():
    print(var.get())

    var.set('ham')
    var2 = ContextVar('var2')
    var2.set('ham2')

ctx = copy_context()
ctx.run(main)
print(ctx[var])

print("len: ", len(ctx))
print(list(iter(ctx)))
