import time


def debug():
    def decorator(f, *args, **kwargs):
        start_time = time.time()
        code, result = f(*args, **kwargs)
        end_time = time.time()
        print('Function name: {}\nTook: {} seconds.'.format(f.__name__, end_time - start_time))
        return code, result
    return decorator
