import requests
import re
import os

def check_update(app):
    r = requests.get(app["check_url"])
    if r.status_code != 200:
        raise Exception("Failed to fetch page")

    match = re.search(r'Version\s*([\d.]+)', r.text, re.IGNORECASE)
    if match:
        return match.group(1)
    raise Exception("Version not found")

def download(app, version):
    url = app["download_url"]
    filename = os.path.join("installers", os.path.basename(url))
    os.makedirs("installers", exist_ok=True)
    r = requests.get(url)
    if r.status_code == 200:
        with open(filename, "wb") as f:
            f.write(r.content)
        return filename
    raise Exception("Download failed")
