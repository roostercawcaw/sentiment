import time
from datetime import datetime

print("Bot started successfully!")

while True:
  now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
  print(f"[{now}] Bot is running.....")
  time.sleep(60)
