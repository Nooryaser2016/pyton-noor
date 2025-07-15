class worker:
    def __init__(self):
        print("this is my constructor")


    def __del__(self):
        print("this is distrctor call")

objs = worker()
del objs
    