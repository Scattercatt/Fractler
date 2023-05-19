import multiprocessing

def worker_function(arg):
    result = arg * 2  # Perform some computation or task
    return result

if __name__ == '__main__':
    pool = multiprocessing.Pool()

    # Submit multiple tasks to the pool using apply_async()
    tasks = [pool.apply_async(worker_function, args=(i,)) for i in range(5)]

    # Get the results from the tasks
    results = [task.get() for task in tasks]

    print("Results:", results)