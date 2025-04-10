import requests
from bs4 import BeautifulSoup
import pandas as pd

# Example: scraping company names from a placeholder website
def scrape_companies():
    companies = []

    # Simulated data scraping
    for i in range(1, 6):
        companies.append({
            "Company Name": f"Company {i}",
            "Contact Person": f"Contact {i}",
            "Industry": "Software",
            "Website": f"https://example{i}.com",
            "Location": "USA",
            "Email": f"contact{i}@example.com"  # <-- Unique email for each lead
        })

    return companies

if __name__ == "__main__":
    data = scrape_companies()
    df = pd.DataFrame(data)
    df.to_csv("data/leads_raw.csv", index=False)
    print("Scraping complete. Raw leads saved to leads_raw.csv")
