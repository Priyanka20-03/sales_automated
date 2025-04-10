import pandas as pd

# Dummy open and click tracking data
clicks = pd.DataFrame({"Email": ["contact1@example.com", "contact3@example.com", "contact5@example.com"]})

clicks.to_csv("data/clicks.csv", index=False)

print("Tracking data created.")
