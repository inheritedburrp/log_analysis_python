import logging

from redis import Redis

class RedisLogger(logging.Handler):
  def __init__(self, host, list_name, port=6379, db=0):
    logging.Handler.__init__(self)
    self.host = host
    self.list_name = list_name
    self.port = port
    self.db = db
    self.r = Redis(host, port=port, db=db)
