
import pandas as pd
import os
import csv
import sys
import psycopg2

def clean_listings(input_path, output_path, city):
    df = pd.read_csv(input_path)

    columns_to_keep = [
        "id", "host_id", "host_name", "neighbourhood_cleansed",
        "latitude", "longitude", "property_type", "room_type",
        "accommodates", "bedrooms", "beds", "bathrooms",
        "price", "minimum_nights", "maximum_nights", "availability_365",
        "number_of_reviews", "last_review", "reviews_per_month", "review_scores_rating",
        "instant_bookable", "host_is_superhost", "calculated_host_listings_count",
        "amenities"
    ]
    df = df[columns_to_keep]

    df["instant_bookable"] = df["instant_bookable"].map({"t": True, "f": False})
    df["host_is_superhost"] = df["host_is_superhost"].map({"t": True, "f": False})
    df["host_is_superhost"] = df["host_is_superhost"].fillna(False)

    df = df.dropna(subset=["price"])
    df["beds"] = df["beds"].fillna(df["beds"].median())
    df["bathrooms"] = df["bathrooms"].fillna(df["bathrooms"].median())
    df["bedrooms"] = df["bedrooms"].fillna(df["bedrooms"].median())
    df["review_scores_rating"] = df["review_scores_rating"].fillna(0)
    df["reviews_per_month"] = df["reviews_per_month"].fillna(0)
    df["host_name"] = df["host_name"].fillna("Unknown")

    df["price"] = df["price"].replace(r"[$,]", "", regex=True).astype(float)

    amenities_list = [
        "Wifi", "Air conditioning", "Heating", "Washer", "Dryer", "TV", "Kitchen",
        "Elevator", "Free parking on premises", "Free street parking", "Crib",
        "Smoke alarm", "Carbon monoxide alarm", "Pool", "Hot tub", "Gym", "Pets allowed"
    ]

    for amenity in amenities_list:
        col_name = amenity.lower().replace(" ", "_").replace("-", "_")
        df[col_name] = df["amenities"].str.contains(amenity, case=False, na=False)

    df.drop(columns=["amenities"], inplace=True)
    df["city"] = city
    df.to_csv(output_path, index=False)
    return df

def get_existing_listing_ids():
    conn = psycopg2.connect(
        host="localhost",
        port=5433,
        dbname="airbnb_project",
        user="postgres",
        password="jorgealves221"
    )
    cur = conn.cursor()
    cur.execute("SELECT id FROM listings")
    ids = [str(row[0]) for row in cur.fetchall()]
    cur.close()
    conn.close()
    return set(ids)

def clean_calendar(input_path, output_path, valid_listing_ids, city):
    df = pd.read_csv(input_path)
    df["listing_id"] = df["listing_id"].astype(str)
    df = df[df["listing_id"].isin(valid_listing_ids)]

    df = df.drop(columns=["adjusted_price", "maximum_nights"], errors="ignore")
    df["date"] = pd.to_datetime(df["date"])
    df["available"] = df["available"].map({"t": True, "f": False})
    df["price"] = df["price"].replace(r"[$,]", "", regex=True).astype(float)
    df["minimum_nights"] = df["minimum_nights"].astype("Int64")
    df["city"] = city

    df.to_csv(output_path, index=False)

def clean_reviews(input_path, output_path, valid_listing_ids, city):
    df = pd.read_csv(input_path)
    df["listing_id"] = df["listing_id"].astype(str)
    df = df[df["listing_id"].isin(valid_listing_ids)]

    df = df.drop(columns=["reviewer_name", "reviewer_id", "comments"], errors="ignore")
    df["date"] = pd.to_datetime(df["date"])
    df = df.dropna()
    df = df.reset_index(drop=True)
    df["review_uid"] = [f"{city.lower()}_{i}" for i in df.index]
    df["city"] = city
    df = df[["review_uid", "id", "listing_id", "date", "city"]]

    df.to_csv(output_path, index=False)

def main():
    if len(sys.argv) < 2:
        print("❌ Please provide a city name. Example: python pipeline_clean_only.py Barcelona")
        sys.exit(1)

    city = sys.argv[1]
    input_dir = f"data/{city}"
    output_dir = "output"
    os.makedirs(output_dir, exist_ok=True)

    listings_in = f"{input_dir}/listings.csv"
    calendar_in = f"{input_dir}/calendar.csv"
    reviews_in = f"{input_dir}/reviews.csv"

    listings_out = f"{output_dir}/cleaned_listings_{city}.csv"
    calendar_out = f"{output_dir}/cleaned_calendar_{city}.csv"
    reviews_out = f"{output_dir}/cleaned_reviews_{city}.csv"

    if os.path.exists(listings_in):
        clean_listings(listings_in, listings_out, city)
    else:
        print(f"❌ Missing file: {listings_in}")

    valid_ids = get_existing_listing_ids()

    if os.path.exists(calendar_in):
        clean_calendar(calendar_in, calendar_out, valid_ids, city)
    else:
        print(f"❌ Missing file: {calendar_in}")

    if os.path.exists(reviews_in):
        clean_reviews(reviews_in, reviews_out, valid_ids, city)
    else:
        print(f"❌ Missing file: {reviews_in}")

    print(f"🎉 Cleaned files created for city: {city} (no data uploaded to PostgreSQL)")

if __name__ == "__main__":
    main()
