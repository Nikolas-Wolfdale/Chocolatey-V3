import re
import requests

def check_update(app):
    url = "https://www.mozilla.org/en-US/firefox/new/"
    html = requests.get(url, timeout=10).text
    match = re.search(r'data-latest-firefox="([\d.]+)"', html)
    return match.group(1) if match else None

def download(app, version):
    url = f"https://download.mozilla.org/?product=firefox-{version}-ssl&os=win64&lang=en-US"
    filename = f"installers/firefox-{version}.exe"
    r = requests.get(url, timeout=20)
    with open(filename, "wb") as f:
        f.write(r.content)
    return filename
