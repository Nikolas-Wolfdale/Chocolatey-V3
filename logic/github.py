import requests
import os

def check_update(app):
    repo = app["check_url"].rstrip("/").split("/")[-2:]
    api_url = f"https://api.github.com/repos/{'/'.join(repo)}/releases/latest"
    r = requests.get(api_url)
    if r.status_code != 200:
        raise Exception("GitHub API request failed")
    data = r.json()
    return data["tag_name"].lstrip("v")

def download(app, version):
    repo = app["check_url"].rstrip("/").split("/")[-2:]
    api_url = f"https://api.github.com/repos/{'/'.join(repo)}/releases/latest"
    r = requests.get(api_url)
    assets = r.json().get("assets", [])
    if not assets:
        raise Exception("No assets found")

    url = assets[0]["browser_download_url"]
    filename = os.path.join("installers", os.path.basename(url))
    os.makedirs("installers", exist_ok=True)

    r = requests.get(url)
    if r.status_code == 200:
        with open(filename, "wb") as f:
            f.write(r.content)
        return filename
    raise Exception("Download failed")
