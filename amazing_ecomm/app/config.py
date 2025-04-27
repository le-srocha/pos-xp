import os

"""Basic connection example.
"""

import redis
import json

#r = redis.Redis(
#    host='redis-19157.c13.us-east-1-3.ec2.redns.redis-cloud.com',
#    port=19157,
#    decode_responses=True,
#    username="default",
#    password="VyUoDmTuULOK1bDT5lK7PPOcHqf7lQp6",
#)

#success = r.hset(1, 'Nome', 'Joao')
#success = r.hset(1, 'Sobrenome', 'Silva')

#success = r.hset(2, 'Nome', 'Maria')
#success = r.hset(2, 'Sobrenome', 'Antonieta')

#success = r.hset(3, 'Nome', 'Joana')
#success = r.hset(3, 'Sobrenome', 'Pacheco')
# True

#for key in r.scan_iter():
#    #print(key)
#    #if key == '3':
#    result = r.hgetall(key)
#    if result['Nome']== 'Heloisa':
#        print(result)

REDIS = '{"URL": "redis-19157.c13.us-east-1-3.ec2.redns.redis-cloud.com", "port": "19157", "username": "default", "password": "VyUoDmTuULOK1bDT5lK7PPOcHqf7lQp6"}'

REDIS_URL = os.getenv('REDIS', REDIS)

#class Config:
#    r = redis.Redis(
#        host='redis-19157.c13.us-east-1-3.ec2.redns.redis-cloud.com',
#        port=19157,
#        decode_responses=True,
#        username="default",
#        password="VyUoDmTuULOK1bDT5lK7PPOcHqf7lQp6",
#    )
#REDIS_URL = os.getenv('REDIS_URL', 'redis-19157.c13.us-east-1-3.ec2.redns.redis-cloud.com')