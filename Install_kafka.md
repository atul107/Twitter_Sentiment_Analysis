                                                    # Kafka(For Ubuntu)

## Prerequisite
### 1. Java
sudo apt update
sudo apt install default-jdk
Download and install kafka                
wget https://www.apache.org/dyn/closer.cgi?path=/kafka/2.2.0/kafka_2.12-2.2.0.tgz 
tar xzf kafka_2.12-1.0.1.tgz
mv kafka_2.12-1.0.1 /usr/local/kafka

Starting kafka server
cd /usr/local/kafka
bin/zookeeper-server-start.sh config/zookeeper.properties
bin/kafka-server-start.sh config/server.properties
Creating kafka topic
bin/kafka-topics.sh --create --zookeeper localhost:2181 --replication-factor 1 --partitions 1 --topic testTopic
bin/kafka-topics.sh --list --zookeeper localhost:2181 (To check the available topics)
Sending message in kafka
bin/kafka-console-producer.sh --broker-list localhost:9092 --topic testTopic
Using kafka consumer
bin/kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic testTopic --from-beginning

