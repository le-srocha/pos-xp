import redis
import json
from app.config import REDIS

def redis_connection():
    conn = json.loads(REDIS)

    r = redis.Redis(
            host=conn["URL"],
            port=conn["port"],
            decode_responses=True,
            username=conn["username"],
            password=conn["password"],
        )
    return r