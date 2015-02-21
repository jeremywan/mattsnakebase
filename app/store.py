import os
import redis

redis_url = os.getenv('REDISTOGO_URL', 'redis://localhost:6379')


def get_redis():
    return redis.from_url(redis_url)
