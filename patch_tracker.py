import requests
import os
from dotenv import load_dotenv

load_dotenv()

webhook_url = os.getenv("DISCORD_WEBHOOK_URL")


url = "https://ddragon.leagueoflegends.com/api/versions.json"

response = requests.get(url)
data = response.json()

if not os.path.exists("last_patch.txt"):
    with open("last_patch.txt", "w") as f:
        f.write(data[0])
else:
    with open("last_patch.txt", "r") as f:
        saved_patch = f.read().strip()

        if saved_patch == data[0]:
            print("There's no new patch.")
        else:
            with open("last_patch.txt", "w") as f:
                f.write(data[0])

            payload = {"content": f"🚨 New Patch {data[0]}!"}
            requests.post(webhook_url, json=payload)
