x = "awesome"


def myfunc():
    global x
    print("Python is " + x)
    x = "fantastic"


myfunc()
print("Phthon is " + x)