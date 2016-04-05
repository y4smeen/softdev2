import random

def htmler(f):
    def inner():
        name = f()
        return "<html>" + name + "</html>"
    return inner

@htmler
def get_name():
    names = ['tom','sue','harry','lisa','sarah','horatio']
    return random.choice(names)

print get_name()
