# RedisDB

## Preparation

I'll prepare a dataset based on [crimes dataset](https://catalog.data.gov/dataset/crime-data-from-2020-to-present). It is about 60mb, so it should be enough to see the differences in speed.

As we use a key-value db, we should prepare the data to match this pattern. So, I'll leave only columns `DR_NO` of integers from 0 to total length and `AREA NAME` of string. So, data looks like this:
```
[
    {
        "DR_NO": 0,
        "AREA NAME": "Wilshire"
    },
    {
        "DR_NO": 1,
        "AREA NAME": "Central"
    },
    {
        "DR_NO": 2,
        "AREA NAME": "Southwest"
    },
    ...
]
```
Make a docker container with redis:
```shell
docker pull redis                                 # pulling latest image
docker run --name redis-server -d redis           # run a container
docker exec -it redis-server [bash | redis-cli]   # enter the container using bash or redis-cli
```
We have a dataset in `/dataset/prepared_crimes_data.json` locally. Move it into the container:
```shell
docker ps  # to get the id of the container
docker cp ./dataset/prepared_crimes_data.json <container_id>:/crimes.json
```

## Queries
Since Redis CLI does not have methods to load jsons, I'll work using python module `redis`. Documentation is [here](https://redis-py.readthedocs.io/en/stable/commands.html).
First, one needs to install python and `redis` module in container:
```shell
apt update
apt install -y python3-redis
```

In python:
```python
import redis

# Connecting to redis
r = redis.Redis(host='localhost', port=6379, db=0)
```

Read json and save it to `crimes_data`:
```python
import json


with open('/crimes.json') as data_file:
    crimes_data = json.load(data_file)
```
Now we're ready to measure latencies. We can do it using `time` module. Functions are written [here](functions.py). I will explain how they work in a few words:

* Every `insert` function uses insert method to insert data in a specific structure
* Every `read` function uses a specific method to get the elements based on the structure

| Structure | Insert method | Parameters                            | Read method | Parameters             |
|-----------|---------------|---------------------------------------|-------------|------------------------|
| string    | set           | key, value                            | get         | key                    |
| hset      | hset          | string with name of hash, key, value  | hget        | name of hash, key      |
| zset      | zadd          | string with zset name, {field: value} | zrange      | name of zset, from, to |
| list      | lpush         | string with name of list, value       | lindex      | name of list, index    | 

Between phases we need to delete all keys in database:
```python
r.flushdb()
```

Let's compare the results:

| Structure | Insertion time, sec | Read num_keys time, sec | Read one key time, sec |
|-----------|---------------------|-------------------------|------------------------|
| string    | 56.03159728099854   | 2.2587938419965212      | 0.0002258793841996521  |
| hset      | 53.940741657002945  | 1.5154052170037176      | 0.00015154052170037176 |
| zset      | 68.10686078899744   | 0.0013905029991292395   | 1.3905029991292395e-07 |
|           |                     | 2.1988472070006537      | 0.00021988472070006538 |
| list      | 52.91529133599397   | 2.594695405001403       | 0.00025946954050014027 |

**Conclusion**: insertion in list is the fastest. Reading from sorted set is fastest, but only because we get a sequence of elements using range from 0 to num_keys. 
If we use per-element get, the best will be, undoubtedly, hash set.

[Next part](cluster.md)
