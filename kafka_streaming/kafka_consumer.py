from kafka import KafkaConsumer
import json
from pymongo import MongoClient

# Connexion à MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client['book_database']
collection = db['books']

# Configuration du consommateur
consumer = KafkaConsumer(
    'books_topic',
    bootstrap_servers='localhost:9092',
    auto_offset_reset='earliest',
    group_id='books-consumer-group'
)

print("Connected to Kafka. Listening...")

# Consommer les messages et les insérer dans MongoDB
for message in consumer:
    book_data = json.loads(message.value.decode('utf-8'))  # Décoder le message JSON
    print(f"Received book: {book_data}")
    
    # Insérer dans MongoDB
    collection.insert_one(book_data)
    print("Book inserted into MongoDB.")
