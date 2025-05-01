""" import streamlit as st
import pandas as pd

df = pd.read_json("../books_scraper/books.json")
df['price'] = df['price'].astype(float)

st.title("📚 Analyse des livres (Books to Scrape)")

st.subheader("Données brutes")
st.dataframe(df)

st.subheader("Statistiques")
st.write(f"Prix moyen : £{df['price'].mean():.2f}")
st.write(f"Nombre total de livres : {len(df)}")

st.subheader("Livres par note")
st.bar_chart(df['rating'].value_counts()) """

import streamlit as st
from pymongo import MongoClient

# Connexion à MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client['book_database']
collection = db['books']

# Titre de l'application Streamlit
st.title('Livres en Temps Réel')

# Afficher les livres
books = collection.find()  # Récupérer tous les livres
for book in books:
    st.write(f"Title: {book.get('title', 'No Title Provided')}")
    st.write(f"Author: {book.get('author', 'No Author Provided')}")
    st.write(f"Price: {book.get('price', 'No Price Provided')}")
    st.write("---")

