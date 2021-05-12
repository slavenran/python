import timeit

start = timeit.default_timer()

def f(x):
    return x*x

print("[{}, {}, {}]".format(f(1), f(2), f(3)))

stop = timeit.default_timer()
print("Time: ", stop - start)