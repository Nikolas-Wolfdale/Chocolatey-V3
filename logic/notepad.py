import re
import requests

def check_update(app):
    html = requests.get(app['check_url'], timeout=10).text
    match = re.search(r'Latest Release.*?Notepad\+\+ ([\d.]+)', html, re.DOTALL)
    return match.group(1) if match else None

def download(app, version):
    url = f"https://github.com/notepad-plus-plus/notepad-plus-plus/releases/download/v{version}/npp.{version}.Installer.x64.exe"
    r = requests.get(url, timeout=20)
    filename = f"installers/npp-{version}.exe"
    with open(filename, "wb") as f:
        f.write(r.content)
    return filename
