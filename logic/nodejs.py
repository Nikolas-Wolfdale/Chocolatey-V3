import requests

def check_update(app):
    json = requests.get("https://nodejs.org/dist/index.json", timeout=10).json()
    for entry in json:
        if entry.get("lts"):
            return entry["version"].lstrip("v")
    return None

def download(app, version):
    url = f"https://nodejs.org/dist/v{version}/node-v{version}-x64.msi"
    r = requests.get(url, timeout=20)
    filename = f"installers/nodejs-{version}.msi"
    with open(filename, "wb") as f:
        f.write(r.content)
    return filename
