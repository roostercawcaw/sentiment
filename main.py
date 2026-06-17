import praw
import os
import smtplib
import urllib.request
from datetime import datetime
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

#Email config from environment variables
EMAIL_ADDRESS = os.environ.get("EMAIL_ADDRESS")
EMAIL_PASSWORD = os.environ.get("EMAIL_PASSWORD")

def get_wsb_posts():
    url = "https://www.reddit.com/r/wallstreetbets/hot.json?limit=10"
    req = urllib.request.Request(url, headers={"User-Agent": "wsb-scraper/1.0"})
    with urllib.request.urlopen(req) as response:
        data = json.loads(response.read().decode())
    posts = []
    for post in data["data"]["chidren"]:
        posts.append(f"⬆️ {p['score']} | {p['title']}")
    return posts

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
    print(f"[{now}] Bot started successfully!")
    
    # This is where scraper output goes later
    try:
        posts = get_wsb_posts()
        body = f"WSB Top Posts - {now}\n\n" + "\n".join(posts)
    except Exception as e:
        body = f"Error fetching posts: {e}"

    print(body)
    print(f"All done!")

    send_email(f"WSB Report - {now}", body)

if __name__ == "__main__":
  main()
