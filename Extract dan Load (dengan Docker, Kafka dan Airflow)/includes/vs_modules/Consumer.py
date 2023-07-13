from kafka import KafkaConsumer
import json

def task():
    # Set up the Kafka consumer
    consumer = KafkaConsumer('tugasde',
                            bootstrap_servers='localhost:9092',
                            auto_offset_reset='earliest',
                            value_deserializer=lambda x: json.loads(json.dumps(x.decode('utf-8'))))

    # Read and process the tweets from the Kafka cluster
    import os
    print (os.getcwd())
    with open('data_twitter.json', 'a') as f:
        for message in consumer:
            tweet = json.dumps(message.value)
            f.write(tweet + '\n')
            print(tweet)

