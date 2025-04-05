# 🏡 Airbnb Data Pipeline Project

This project builds a complete end-to-end data pipeline using Airbnb open data. It involves extracting raw `.csv` files for multiple cities, cleaning and transforming the data using Python, storing it in a SQL database, and analyzing it through SQL queries and Tableau dashboards.

## 🚀 Goal

To demonstrate strong skills in:
- **Data Engineering**: Data pipeline, automation, SQL database integration
- **Data Analysis**: EDA, cleaning, merging datasets, business questions
- **Visualization**: Interactive dashboards in Tableau
- **Version Control**: Git + GitHub workflow with a clean project structure

---

## 🗂️ Data Sources

All data comes from [Inside Airbnb](http://insideairbnb.com/get-the-data/), and includes multiple cities.

Each city includes:
- `listings.csv` – Listing details (price, host, availability, etc.)
- `calendar.csv` – Daily availability & price per listing
- `reviews.csv` – User reviews and timestamps

---

## 🧱 Project Structure

```
Airbnb Project/
│
├── data/                  # Raw data by city
│   ├── amsterdam/
│   ├── lisbon/
│   └── ...
│
├── notebooks/             # Jupyter notebooks for EDA & validation
│
├── output/                # Cleaned data ready for SQL
│
├── pipeline/              # ETL scripts to automate loading/cleaning
│
├── sql/                   # Schema creation & query scripts
│
└── README.md              # You are here
```

---

## 🔄 Pipeline Workflow

1. **Extract**: Download `.csv` files for each city
2. **Transform**: Clean & normalize fields using Python (handle nulls, data types, etc.)
3. **Load**: Insert data into a local or cloud SQL database
4. **Analyze**: Use SQL to answer business questions
5. **Visualize**: Build Tableau dashboards with KPIs and trends

---

## 📊 Example Tableau Dashboard

▶️ [Explore the dashboard](https://public.tableau.com/views/BurdenedbyWeight_HowHighBMIInfluencesDeathsfromMajorNoncommunicableDiseases/IschemicDash)

---

## ✅ Status

- [x] Data folders & structure set
- [x] Git repository initialized & connected
- [ ] First city pipeline in progress
- [ ] SQL schema definition
- [ ] Tableau connection to database

---

## 👨‍💻 Author

Bruno Ramos  
📍 Based in Amsterdam, relocating to Munich  
💬 Let’s connect: brunoramos321
