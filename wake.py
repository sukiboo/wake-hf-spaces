import yaml
import requests

with open("config.yml") as f:
    config = yaml.safe_load(f)

username = config["hf_username"]

spaces = requests.get(
    "https://huggingface.co/api/spaces",
    params={"author": username},
    timeout=30,
).json()

for space in spaces:
    subdomain = space["id"].replace("/", "-").lower()
    url = f"https://{subdomain}.hf.space/"
    try:
        r = requests.get(url, timeout=60)
        print(f"{r.status_code} {url}")
    except Exception as e:
        print(f"ERR {url}: {e}")
