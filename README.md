# Twitter_Sentiment_Analysis
Real time sentiment analysis in kafka using twitter's streaming api


## A. Prerequisite
### 1. Java
#### Installing Java 
Install by running following commands
```
sudo apt update
```
```
sudo apt install default-jdk
```
### Kafka
#### B. Installing Kafka (Ubuntu)
Download and install kafka
```
wget https://www.apache.org/dyn/closer.cgi?path=/kafka/2.2.0/kafka_2.12-2.2.0.tgz 
```
```
tar xzf kafka_2.12-1.0.1.tgz
```
```
mv kafka_2.12-1.0.1 /usr/local/kafka
```
Starting kafka server
```
cd /usr/local/kafka
```
```
bin/zookeeper-server-start.sh config/zookeeper.properties
```
```
bin/kafka-server-start.sh config/server.properties
```
Creating kafka topic
```
bin/kafka-topics.sh --create --zookeeper localhost:2181 --replication-factor 1 --partitions 1 --topic testTopic
```
```
bin/kafka-topics.sh --list --zookeeper localhost:2181 (To check the available topics)
```
Sending message in kafka
```
bin/kafka-console-producer.sh --broker-list localhost:9092 --topic testTopic
```
Using kafka consumer
```
bin/kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic testTopic --from-beginning
```
### Elasticsearch
Download the latest version from https://www.elastic.co/downloads/ and 
extract the downloaded file.
#### Running Elasticsearch
```
cd 'Extracted folder'
```
```
bin/elasticsearch
```

### Kibana
Download the version compatible with the version of elasticsearch you have downloaded and extract it.
#### Running kibana
```
cd 'Extracted folder
```
```
bin/kibana
```


