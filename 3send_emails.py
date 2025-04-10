import pandas as pd
import smtplib
from email.mime.text import MIMEText
from jinja2 import Template
import time

# Email configuration
SENDER_EMAIL = "azby9269@gmail.com"   
SENDER_PASSWORD = "cyxydghqculoqbty"  
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587

# Load leads
df = pd.read_excel("data/leads.xlsx")

# Load email template
with open("templates/email_template.html", "r") as file:
    template = Template(file.read())

def send_email(recipient, subject, body):
    msg = MIMEText(body, 'html')
    msg['Subject'] = subject
    msg['From'] = SENDER_EMAIL
    msg['To'] = recipient

    with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
        server.starttls()
        server.login(SENDER_EMAIL, SENDER_PASSWORD)
        server.send_message(msg)
        print(f"Email sent to {recipient}")

for index, row in df.iterrows():
    body = template.render(
        name=row["Contact Person"],
        company=row["Company Name"],
        industry=row["Industry"]
    )
    send_email(row["Email"], "Grow Your Business with AI", body)
    time.sleep(5)
