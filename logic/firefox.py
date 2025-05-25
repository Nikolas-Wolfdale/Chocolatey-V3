import re
import requests

def check_update(app):
    response = requests.get(app['check_url'], timeout=10)
    match = re.search(r'Latest Firefox.*?Download Firefox ([\d.]+)', response.text, re.DOTALL)
    return match.group(1) if match else None

def download(app, version):
    url = f"https://download.mozilla.org/?product=firefox-{version}-ssl&os=win64&lang=en-US"
    r = requests.get(url, timeout=20)
    filename = f"installers/firefox-{version}.exe"
    with open(filename, "wb") as f:
        f.write(r.content)
    return filename
