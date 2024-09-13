import redis


def init_redis():
    redis_client = redis.Redis(host='localhost', port=6379, decode_responses=True)
    return redis_client
