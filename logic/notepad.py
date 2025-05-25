import re
import requests

def check_update(app):
    url = "https://notepad-plus-plus.org/downloads/"
    html = requests.get(url, timeout=10).text
    match = re.search(r'/downloads/v([\d.]+)/', html)
    return match.group(1) if match else None

def download(app, version):
    url = f"https://github.com/notepad-plus-plus/notepad-plus-plus/releases/download/v{version}/npp.{version}.Installer.x64.exe"
    filename = f"installers/npp-{version}.exe"
    r = requests.get(url, timeout=20)
    with open(filename, "wb") as f:
        f.write(r.content)
    return filename
