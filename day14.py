from pathlib import Path
p = Path("app.log")
print(p.exists())
print(p.read_text(encoding="utf-8"))
print(p.name)