import re
import requests

def check_update(app):
    html = requests.get(app['check_url'], timeout=10).text
    match = re.search(r'Current Version: ([\d.]+)', html)
    return match.group(1) if match else None

def download(app, version):
    url = app['download_url'].replace("{version}", version)
    r = requests.get(url, timeout=20)
    filename = f"installers/pgadmin-{version}.exe"
    with open(filename, "wb") as f:
        f.write(r.content)
    return filename