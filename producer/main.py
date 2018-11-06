import requests
import json
from kafka import KafkaProducer

apiUrl = "https://api.stackexchange.com/2.2/questions?pagesize=5&order=desc&sort=creation&tagged=neo4j&site=stackoverflow&filter=!5-i6Zw8Y)4W7vpy91PMYsKM-k9yzEsSC1_Uxlf"

resp = requests.get(apiUrl, headers = {"accept":"application/json"}).json()

def publish_message(producer, topic_name, key, body):
    try:
        producer.send(topic_name, key=b'raw', value=body)
        producer.flush()
        print('successfully published Kafka message')
    except Exception as ex:
        print('failed to publish message to Kafka: ', str(ex))

def connect_kafka_producer():
    producer = None

    try:
        producer = KafkaProducer(bootstrap_servers='kafka1:9092', value_serializer=lambda v: json.dumps(v).encode('utf-8'))
    except Exception as ex:
        print('failed to connect to Kafka: ', str(ex))
    finally:
        return producer

producer = connect_kafka_producer()
publish_message(producer, 'questions', 'raw', resp)
