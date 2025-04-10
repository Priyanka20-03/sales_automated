import pandas as pd

# Load original leads
leads = pd.read_excel("data/leads.xlsx")

# Load tracking data
clicks = pd.read_csv("data/clicks.csv")

# Add engagement columns
leads['Clicked'] = leads['Email'].isin(clicks['Email'])

# Categorize
def categorize(row):
    if row['Clicked']:
        return 'Hot Lead'
    else:
        return 'Cold Lead'

leads['Lead Status'] = leads.apply(categorize, axis=1)

# Save categorized leads
leads.to_excel("output/categorized_leads.xlsx", index=False)
print("Leads categorized and saved.")

