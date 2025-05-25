import re
import requests

def check_update(app):
    html = requests.get(app['check_url'], timeout=10).text
    match = re.search(r'Latest Python 3 Release - Python ([\d.]+)', html)
    return match.group(1) if match else None

def download(app, version):
    url = f"https://www.python.org/ftp/python/{version}/python-{version}-amd64.exe"
    r = requests.get(url, timeout=20)
    filename = f"installers/python-{version}.exe"
    with open(filename, "wb") as f:
        f.write(r.content)
    return filename