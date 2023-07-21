import time

def timeit(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} ran in {end - start} seconds.")
        return result
    return wrapper

@timeit
def long_running_func():
    time.sleep(2)

long_running_func()
