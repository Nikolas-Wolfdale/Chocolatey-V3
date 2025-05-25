import json
import importlib
import os
from datetime import datetime

with open("apps.json", encoding="utf-8") as f:
    apps = json.load(f)

for app in apps:
    print(f"🔍 Checking {app['name']}...")
    try:
        module = importlib.import_module(f"logic.{app['type']}")
        actual_version = module.check_update(app)
        app['last_check'] = datetime.now().isoformat()

        if actual_version and actual_version != app['current_version']:
            app['actual_version'] = actual_version
            print(f"⬆️  Update found: {actual_version}")
            path = module.download(app, actual_version)
            print(f"📦 Downloaded to: {path}")
            app['current_version'] = actual_version
            app['last_update'] = datetime.now().isoformat()
        else:
            print("✅ Up to date.")
    except Exception as e:
        print(f"❌ Failed to update {app['name']}: {e}")

with open("apps.json", "w", encoding="utf-8") as f:
    json.dump(apps, f, indent=2, ensure_ascii=False)

