from .observer import Observer
class ObserverTest(object):
    def update(self, *args, **kwargs):
        print("Observer Test received: {0}\n{1}".format(args, kwargs))
