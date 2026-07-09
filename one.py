def outer():
    def inner():
        print("Inner function")
    return inner
inner=outer()
inner()
inner()
inner()