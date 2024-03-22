import time


def get_insert_time(r, data, type_of_struct):
    if type_of_struct == 'string':
        return get_insert_time_srt(r, data)
    elif type_of_struct == 'hset':
        return get_insert_time_hash(r, data)
    elif type_of_struct == 'zset':
        return get_insert_time_sort(r, data)
    elif type_of_struct == 'list':
        return get_insert_time_list(r, data)
    else:
        raise "Unknown type of insertion!"


def get_insert_time_srt(r, data):
    t1 = time.perf_counter()
    for entry in data:
        r.set(entry.get('DR_NO'), entry.get('AREA NAME'))
    t2 = time.perf_counter()
    return f"Insertion with string structure took {t2 - t1}"


def get_insert_time_hash(r, data):
    t1 = time.perf_counter()
    for entry in data:
        r.hset('myhash', entry.get('DR_NO'), entry.get('AREA NAME'))
    t2 = time.perf_counter()
    return f"Insertion with hash structure took {t2 - t1}"


def get_insert_time_sort(r, data):
    t1 = time.perf_counter()
    for entry in data:
        r.zadd('myzset', {entry.get('AREA NAME'): entry.get('DR_NO')})
    t2 = time.perf_counter()
    return f"Insertion with sorted structure took {t2 - t1}"


def get_insert_time_list(r, data):
    t1 = time.perf_counter()
    for entry in data:
        r.lpush('mylist', entry.get('AREA NAME'))
    t2 = time.perf_counter()
    return f"Insertion with sorted structure took {t2 - t1}"


def get_read_time(r, type_of_struct, num_keys=10000):
    if type_of_struct == 'string':
        return get_read_time_str(r)
    elif type_of_struct == 'hset':
        return get_read_time_hash(r)
    elif type_of_struct == 'zset':
        return get_read_time_sort(r)
    elif type_of_struct == 'list':
        return get_read_time_list(r)
    else:
        raise "Unknown type of insertion!"


def get_read_time_str(r, num_keys=10000):
    t1 = time.perf_counter()
    for i in range(num_keys):
        r.get(i)
    t2 = time.perf_counter()
    return f"Total read time of {num_keys} elements: {t2 - t1}\nAverage per element: {(t2 - t1) / num_keys}"


def get_read_time_hash(r, num_keys=10000):
    t1 = time.perf_counter()
    for i in range(num_keys):
        r.hget('myhash', i)
    t2 = time.perf_counter()
    return f"Total read time of {num_keys} elements: {t2 - t1}\nAverage per element: {(t2 - t1) / num_keys}"


def get_read_time_sort(r, num_keys=10000):
    t1 = time.perf_counter()
    for i in range(num_keys):
        r.zrange('myzset', i, i+1)
    t2 = time.perf_counter()
    return f"Total read time of {num_keys} elements: {t2 - t1}\nAverage per element: {(t2 - t1) / num_keys}"


def get_read_time_list(r, num_keys=10000):
    t1 = time.perf_counter()
    for i in range(num_keys):
        r.lindex('mylist', i)
    t2 = time.perf_counter()
    return f"Total read time of {num_keys} elements: {t2 - t1}\nAverage per element: {(t2 - t1) / num_keys}"
