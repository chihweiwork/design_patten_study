import time, datetime
from functools import wraps
import logging

#logging.basicConfig(level=logging.INFO, filename='log.txt', filemode='w',
logging.basicConfig(
        level=logging.INFO,
	format='[%(asctime)s] [%(levelname)s] %(message)s',
	datefmt='%Y-%m-%d %H:%M:%S',
	)

def timeit(func):
    @wraps(func)
    def timeit_wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        total_time = end_time - start_time
        logging.info(f'Function {func.__name__}{args} {kwargs} Took {total_time:.4f} seconds')
        return result
    return timeit_wrapper

def start_end(func):
    @wraps(func)
    def print_log(*args, **kwargs):
        logging.info(f"Start function : {func.__name__}")
        result =  func(*args, **kwargs)
        logging.info(f"Finish function : {func.__name__}")
        return result
    return print_log
