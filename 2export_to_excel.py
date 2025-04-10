import pandas as pd

def export_to_excel():
    df = pd.read_csv("data/leads_raw.csv")
    df.to_excel("data/leads.xlsx", index=False)
    print("Exported data to Excel: leads.xlsx")

if __name__ == "__main__":
    export_to_excel()
