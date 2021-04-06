import os
import redis

class CrawlerQueue:

    def __init__(self):
        self._redis = redis.from_url(os.environ.get("REDIS_URL"))

    def append(self, url: str) -> "CrawlerQueue":
        l = self._redis.get("crawler_queue_length") if self._redis.exists("crawler_queue_length") else 0
        self._redis.set("crawler_queue_length", l + 1)
        return self

    def __len__(self) -> int:
        return int(self._redis.get("crawler_queue_length"))