from kafka import KafkaProducer
import json

producer = KafkaProducer(bootstrap_servers='localhost:9092',
                         value_serializer=lambda x: json.dumps(x).encode('utf-8'))

with open('../books_scraper/books.json', 'r') as f:
    books = json.load(f)

for book in books:
    producer.send('books_topic', value=book)
    print(f"Sent book: {book}") 


producer.flush()