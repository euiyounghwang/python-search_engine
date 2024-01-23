import os

class Settings:
    """
    environment: str = os.getenv("ENVIRONMENT", "dev")
    testing: str = os.getenv("TESTING", "0")
    redis_url: AnyUrl = os.environ.get("REDIS_URL", "redis://redis")
    redis_password: str = os.getenv("REDIS_PASSWORD", "redis_pass")
    redis_db: int = int(os.getenv("REDIS_DB", "0"))
    redis_hash: str = os.getenv("REDIS_TEST_KEY", "covid-19-test")
    up: str = os.getenv("UP", "up")
    down: str = os.getenv("DOWN", "down")
    web_server: str = os.getenv("WEB_SERVER", "web_server")
    """
    def __init__(self, logger, doc):
        self.logger = logger
        self.doc = doc
        
        # Read_Doc with arguments from Docker -e option
        self.hosts: str = os.getenv("ES_HOST", doc['app']['es']['es_host'])
        self.kafka_hosts = str(os.getenv("KAFKA_HOST", doc['app']['kafka']['host'])).split(",")
        self.kafka_topics = str(os.getenv("KAFKA_TOPIC", doc['app']['kafka']['topic'])).split(",")
        self.logger.info(f'@@elasticsearch.hosts - {self.hosts}, kafka_hosts : {self.kafka_hosts}')
        
    def get_Hosts(self):
        return self.hosts
    
    def get_Kafka_Hosts(self):
        return self.kafka_hosts
    
    def get_Kafka_topic(self):
        return self.kafka_topics
