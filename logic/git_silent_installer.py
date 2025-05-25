import re
import requests

def check_update(app):
    # Получаем страницу релизов
    html = requests.get("https://github.com/git-for-windows/git/releases/latest", timeout=10).text
    # Ищем версию из заголовка "Git for Windows vX.Y.Z.windows.1"
    match = re.search(r'Git for Windows v([\d.]+)\.windows\.1', html)
    return match.group(1) if match else None

def download(app, version):
    full_version = f"{version}.windows.1"
    url = f"https://github.com/git-for-windows/git/releases/download/v{full_version}/Git-{version}-64-bit.exe"
    filename = f"installers/git-{version}.exe"
    r = requests.get(url, timeout=20)
    r.raise_for_status()
    with open(filename, "wb") as f:
        f.write(r.content)
    return filename
