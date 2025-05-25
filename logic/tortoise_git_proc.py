import requests
import re

def check_update(app):
    html = requests.get(app['check_url'], timeout=10).text
    match = re.search(r'TortoiseGit ([\d.]+)', html)
    return match.group(1) if match else None

def download(app, version):
    url = f"https://download.tortoisegit.org/tgit/{version}/TortoiseGit-{version}-64bit.msi"
    r = requests.get(url, timeout=20)
    filename = f"installers/tortoisegit-{version}.msi"
    with open(filename, "wb") as f:
        f.write(r.content)
    return filename
