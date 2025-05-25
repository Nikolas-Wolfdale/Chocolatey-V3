import re
import requests

def check_update(app):
    html = requests.get(app['check_url'], timeout=10).text
    match = re.search(r'Git for Windows ([\d.]+)', html)
    return match.group(1) if match else None

def download(app, version):
    url = f"https://github.com/git-for-windows/git/releases/download/v{version}.windows.1/Git-{version}-64-bit.exe"
    r = requests.get(url, timeout=20)
    filename = f"installers/git-{version}.exe"
    with open(filename, "wb") as f:
        f.write(r.content)
    return filename
