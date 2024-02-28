import requests
from supabase import create_client, Client

# Supabase setup
url: str = "your_supabase_url"
key: str = "your_supabase_key"
supabase: Client = create_client(url, key)

# Function to fetch current prices
def fetch_prices():
    api_url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin,ethereum,ripple&vs_currencies=usd"
    response = requests.get(api_url)
    prices = response.json()
    return {
        "bitcoin": prices["bitcoin"]["usd"],
        "ethereum": prices["ethereum"]["usd"],
        "ripple": prices["ripple"]["usd"],
    }

# Function to compare and update prices
def compare_and_update():
    current_prices = fetch_prices()
    stored_prices = supabase.table("your_table_name").select("*").execute()

    # Assuming stored_prices returns a list of dictionaries
    for row in stored_prices.data:
        # Compare and update logic here
        print(f"Current: {current_prices}, Stored: {row}")

        # Update logic
        # if current_prices['bitcoin'] != row['bitcoin']:
        #     # Update in Supabase

if __name__ == "__main__":
    compare_and_update()
