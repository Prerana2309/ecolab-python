import time

def cached(fn):
    cache={}

    def wrapper(n):
        if n in cache:
            return cache[n]
        result =fn(n)
        cache[n]=result
        return result
    return wrapper

def performance_monitor(fn):
    def inner(n):
        start_time = time.time()
        result = fn(n)
        end_time = time.time()
        time_taken = end_time - start_time
        print(f'Factorial of {n} took {time_taken:.3f}')
        return result
    return inner

@performance_monitor
@cached
def factorial(n):
    func = 1
    for i in range(1, n+1):
        time.sleep(0.5)
        func *= i
    return func

r1=factorial(5)
print(r1)
r2=factorial(7)
print(r2)
r3=factorial(5)
print(r3)