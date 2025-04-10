# Sales Process Automation using Python and AI/ML

This project automates the sales outreach workflow using Python scripts for scraping, emailing, engagement tracking, and lead analytics. The automation reduces manual effort and boosts sales team efficiency by categorizing and analyzing leads based on interaction behavior.


---

## 📁 Project Structure

SALES_AUTOMATED_PROJECT/
│
├── data/
│   ├── clicks.csv
│   ├── leads_raw.csv
│   ├── leads.xlsx
│   └── opens.csv
│
├── output/
│   ├── categorized_leads.xlsx
│   └── email_campaign_report.xlsx
│
| 
│   ├── 1scrape_data.py          # Simulates web scraping and adds email IDs
│   ├── 2export_to_excel.py      # Converts raw scraped data into Excel format
│   ├── 3send_emails.py          # Sends personalized emails using an HTML template
│   ├── 4test_case.py            # Contains test cases (manual)
│   ├── 5categorize_leads.py     # Categorizes leads as Hot,Cold
│   └── 6generate_report.py      # Generates analytics reports from engagement data
│
├── templates/
│   └── email_template.html      # Email body with placeholders (Jinja2-based)
│
└── README.md                    # Project documentation


---


## 🚀 Workflow Overview

### 1. Scraping Leads (`1scrape_data.py`)
Simulates lead scraping and includes:
- Company Name
- Contact Person
- Industry
- Website
- Location
- Unique Email ID

📦 Libraries: `requests`, `BeautifulSoup`, `pandas`

---

### 2. Export to Excel (`2export_to_excel.py`)
Converts the raw leads CSV into Excel format for compatibility and structured storage.

---

### 3. Send Emails (`3send_emails.py`)
- Loads and customizes an HTML email template using `Jinja2`
- Sends emails via `smtplib`
- Tracking links for open and click tracking 

---

### 4. Test Case (`4test_case.py`)
Can include dummy inputs, print checks, or unit tests to validate functionality.

---

### 5. Categorize Leads (`5categorize_leads.py`)
Classifies each lead as:
- **Hot Lead**: Opened
- **Cold Lead**: No interaction

🔁 Uses:
- `opens.csv`
- `clicks.csv`

📦 Library: `pandas`

---

### 6. Generate Report (`6generate_report.py`)
Generates a performance report with:
- Total Emails Sent
- Open Rate
- Click-through Rate
- Hot Leads
- Cold Leads

Outputs:
- `categorized_leads.xlsx`
- `email_campaign_report.xlsx`

---

## 📌 Libraries Used

|     Area          |               Library       | 
|-------------------|-----------------------------|
| Core Programming  | `Python`                      |
| Data Handling     | `pandas`, `openpyxl`        |
| Email Automation  | `smtplib`, `email.mime`     |
| Web Scraping      | `BeautifulSoup`, `requests` |
| Template Rendering| `jinja2`                    |
| File Formats      | `CSV`, `Excel`, `HTML`            |

---

## 💡 Future Scope (AI/ML Integration)

- Apply clustering (e.g., KMeans) for behavioral segmentation

---

## ⚙️ Setup Instructions

1.Install dependencies from Requirement.txt

2. Run Scripts in following sequence : 

python scripts/1scrape_data.py
python scripts/2export_to_excel.py
python scripts/3send_emails.py
python scripts/5categorize_leads.py
python scripts/6generate_report.py
