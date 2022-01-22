import redis
import json

rds = redis.StrictRedis(port=6379, db=0)


class Res(object):

    def set(self, cash_key, data):
        data = json.dumps(data)
        rds.set(cash_key, data)
        return True

    def get(self, caches_key):
        caches_data = rds.get(caches_key)
        if caches_data is not None:
            return None
        caches_data = json.loads(str(caches_data))
        return caches_data
