import time
from datetime import datetime
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

#Email config from environment variables
EMAIL_ADDRESS = os.environ.get("EMAIL_ADDRESS")
EMAIL_PASSWORD = os.environ.get("EMAIL_PASSWORD")

def send_email(subject, body):
    msg = MIMEMultipart()
    msg["From"] = EMAIL_ADDRESS
    msg["To"] = EMAIL_ADDRESS
    msg["Subject"] = subject

    msg.attach(MIMEText(body, "plain"))

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
      server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
      server.sendmail(EMAIL_ADDRESS, EMAIL_ADDRESS, msg.as_string())

    print("Email sent successfully!")

def main():
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # This is where scraper output goes later
    print("Bot started successfully!")
    print(f"[{now}] Bot is ran successfully!")
    print(f"All done!")

    output = f"""
Bot Report - {now}

Status: Running successfully✅
Next step: Reddit + crypto sentiment data will appear here

"""
    print(output)
    send_email(
        subject=f"Bot Report - {now}",
        body=output
    )

if __name__ == "__main__":
  main()

