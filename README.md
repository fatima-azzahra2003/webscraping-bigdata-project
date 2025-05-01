
# 🕸️ Web Scraping & Big Data Pipeline 📊

Ce projet complet montre comment collecter, traiter et visualiser des données en temps réel à partir de sites web de livres.

## 🚀 Technologies utilisées

- **Scrapy** : pour extraire des données de livres (titre, prix, auteur…)
- **Kafka** : pour publier les données extraites dans un flux temps réel
- **MongoDB** : pour stocker les données de manière structurée
- **Streamlit** : pour afficher les livres dans une application web simple
- **Power BI** : pour visualiser dynamiquement les données (filtres, graphiques, tendances)
- **Docker** : pour gérer Kafka/Zookeeper dans des conteneurs
- **Python** : langage principal pour les scripts (Scrapy, Kafka, Streamlit)

## 📁 Structure du projet

```
webscraping_project/
├── books_scraper/         # Scrapy spider
├── kafka_streaming/       # kafka_producer.py et kafka_consumer.py
├── streamlit_app/         # app.py (interface utilisateur)
├── docker-compose.yml     # Pour lancer Kafka + Zookeeper
├── books.json             # Fichier exporté des livres (pour Power BI)
└── README.md
```

## 🔧 Instructions de démarrage

1. **Lancer Kafka & Zookeeper** :

```bash
docker-compose up -d
```

2. **Lancer le producteur Kafka** :

```bash
cd kafka_streaming
python kafka_producer.py
```

3. **Lancer le consommateur Kafka** :

```bash
python kafka_consumer.py
```

4. **Lancer Streamlit** :

```bash
cd ../streamlit_app
streamlit run app.py
```

5. **Visualiser dans Power BI** :
   - Ouvrir Power BI Desktop
   - Importer `books.json`
   - Créer vos visualisations (graphes, filtres, etc.)

## 📸 Résultat

📷 Exemple de dashboard Power BI + Streamlit dans `screenshots/`
## Aperçu du Tableau de Bord Streamlit

![Streamlit Dashboard](screenshots/streamlit_dashboard.png)

## Visualisation avec Power BI

![Power BI Overview](screenshots/powerbi_overview.png)

## 📣 Auteur

Développé par [Fatima-Azzahra Hamdaoui](www.linkedin.com/in/fatima-azzahra-hamdaoui-38a402298)


