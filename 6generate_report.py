import pandas as pd

leads = pd.read_excel("output/categorized_leads.xlsx")

total = len(leads)
clicked = leads['Clicked'].sum()
hot_leads = (leads['Lead Status'] == 'Hot Lead').sum()
cold_leads = (leads['Lead Status'] == 'Cold Lead').sum()

report = {
    "Total Emails Sent": total,
    "Click-through Rate": f"{clicked / total * 100:.2f}%",
    "Hot Leads": hot_leads,
    "Cold Leads": cold_leads
}

report_df = pd.DataFrame(report.items(), columns=["Metric", "Value"])
report_df.to_excel("output/email_campaign_report.xlsx", index=False)

print("Analytics report generated.")
