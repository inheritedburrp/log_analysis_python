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

if __name__ == "__main__":
  import logging
  import logging.config

  logging.config.fileConfig("logging.conf.example")
  
  logger = logging.getLogger("root")
 
  print "Logging a message, both to a file (access.log) and also lpush the same string to a redis list (q:demo in db=10)"
  print "These are defined in the example logging.conf.example file for reference"
  logger.info("Testing the dual logging abilities - to a file and to a redis list")
