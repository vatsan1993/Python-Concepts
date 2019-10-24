from functools import wraps
def my_logger(orig_funct):
    import logging
    logging.basicConfig(filename=f'{orig_funct.__name__}.log',level=logging.INFO)
    @wraps(orig_funct)
    def wrapper(*args, **kwargs):
        logging.info(f'worked with the arguments {args} and {kwargs} ')
        return orig_funct(*args,**kwargs)
    return wrapper



@my_logger
def my_logger_test(name, **kwargs):
    print("Logging is performed.")


my_logger_test("srivasan", age=20)
