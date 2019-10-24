
from  functools import wraps
class mytimer(object):
    def __init__(self, funct):
        self.funct= funct

    def __call__(self, *args, **kwargs):
        import time
        t1= time.time()
        function_result= self.funct(*args, **kwargs)
        t2=  '{:06f}'.format(time.time()-t1)
        print(f'Thee function {self.funct.__name__} executed in {t2} secs')
        return function_result


@mytimer
def forLoop():
    import time
    time.sleep(1)
    mylist=[]
    for i in range(100000):
        mylist.append(i)

@mytimer
def listComprehension():
    import time
    time.sleep(2)
    mylist=[i for i in range(100000)]

forLoop()

listComprehension()
