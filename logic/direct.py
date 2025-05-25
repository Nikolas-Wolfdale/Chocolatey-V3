import requests
import os

def check_update(app):
    # Direct types usually don't provide version info
    return None

def download(app, version):
    url = app['download_url']
    filename = os.path.join("installers", os.path.basename(url))
    os.makedirs("installers", exist_ok=True)

    r = requests.get(url)
    if r.status_code == 200:
        with open(filename, "wb") as f:
            f.write(r.content)
        return filename
    raise Exception("Failed to download file")
