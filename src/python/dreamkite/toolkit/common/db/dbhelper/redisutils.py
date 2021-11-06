import redis


class RedisDBConfig:
    HOST = '127.0.0.1'
    PORT = 6379
    MAX_CONNECTIONS = 1000


class RedisConnection:
    @staticmethod
    def get_connect_pool():
        return redis.ConnectionPool(host=RedisDBConfig.HOST, port=RedisDBConfig.PORT,
                                    max_connections=RedisDBConfig.MAX_CONNECTIONS)

    def get_redis_connection(self, password=None):
        pool = self.get_connect_pool()
        return redis.Redis(connection_pool=pool, password=password)


if __name__ == '__main__':
    client = RedisConnection().get_redis_connection()
    client02 = RedisConnection().get_redis_connection()
