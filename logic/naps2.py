import requests

def check_update(app):
    api = "https://api.github.com/repos/cyanfish/naps2/releases/latest"
    json = requests.get(api, timeout=10).json()
    return json["tag_name"].lstrip("v")

def download(app, version):
    url = f"https://github.com/cyanfish/naps2/releases/download/v{version}/naps2-{version}-setup.exe"
    r = requests.get(url, timeout=20)
    filename = f"installers/naps2-{version}.exe"
    with open(filename, "wb") as f:
        f.write(r.content)
    return filename
