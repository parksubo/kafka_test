from kafka import KafkaProducer
# producer 인스턴스화
# kafka는 클러스터 환경에서 동작하기 때문에 여러개의 서버로 데이터를 보낼 수 있다.
producer = KafkaProducer(bootstrap_servers = ['localhost:9092'])

# 메시지는 byte형태로 보내기
producer.send('first-topic', b'hello world test 2')
# Remove Buffer
producer.flush()